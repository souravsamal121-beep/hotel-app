{
    "name": "Restaurant Website Theme",
    "version": "17.0.1.0.0",
    "category": "Website/Theme",
    "summary": "Restaurant website snippets and theme",
    "description": "\n        Restaurant Website Theme\n        ========================\n        This module provides restaurant-themed website snippets including:\n        - Hero carousel with food imagery\n        - Featured product sections (Breakfast, Main Dishes, Dessert, Special)\n        - Chef showcase section\n        - Product slider\n        - Parallax experience sections\n\n        Images are loaded dynamically - if they exist in the database they will be displayed,\n        otherwise the sections will work without them.\n    ",
    "author": "Custom",
    "website": "",
    "license": "LGPL-3",
    "depends": [
        "website",
        "website_sale"
    ],
    "data": [
        "data/website_homepage.xml"
    ],
    "images": [
        "static/description/icon.png"
    ],
    "installable": True,
    "application": False,
    "auto_install": False
}