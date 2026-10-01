# -*- coding: utf-8 -*-
from odoo import models, api
import logging

_logger = logging.getLogger(__name__)


class Website(models.Model):
    _inherit = 'website'

    @api.model
    def _check_image_exists(self, image_path):
        """Check if an image exists in the system by its path.

        Args:
            image_path: The /web/image/... path

        Returns:
            bool: True if image exists, False otherwise
        """
        try:
            # Extract image ID from path like /web/image/1484-a49beee4/...
            parts = image_path.split('/')
            if len(parts) >= 3:
                img_id_part = parts[3] if len(parts) > 3 else parts[-1]
                # Handle hash format like 1484-a49beee4
                if '-' in img_id_part:
                    img_id = img_id_part.split('-')[0]
                    try:
                        img_id = int(img_id)
                        attachment = self.env['ir.attachment'].sudo().search([
                            ('id', '=', img_id),
                            ('type', '=', 'binary')
                        ], limit=1)
                        return bool(attachment)
                    except ValueError:
                        pass
            return False
        except Exception as e:
            _logger.warning("Error checking image %s: %s", image_path, str(e))
            return False


class IrAttachment(models.Model):
    _inherit = 'ir.attachment'

    @api.model_create_multi
    def create(self, vals_list):
        """Override create to log when restaurant images are being loaded."""
        records = super(IrAttachment, self).create(vals_list)
        for record in records:
            if record.name and any(x in record.name.lower() for x in ['restaurant', 'food', 'chef', 'breakfast', 'dessert']):
                _logger.info("Restaurant theme image created: %s (ID: %s)", record.name, record.id)
        return records
