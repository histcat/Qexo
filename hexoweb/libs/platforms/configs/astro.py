# https://valaxy.site/
config = {
    "name": "Astro",
    "posts": {
        "path": ["src/content/blog"],
        "depth": [-1],
        "type": [".md"],
        "save_path": "src/content/blog/${filename}.md",
        "scaffold": ""
    },
    "drafts": {
        "path": [],
        "depth": [],
        "type": [],
        "save_path": None,
        "scaffold": ""
    },
    "pages": {
        "path": ["src/pages"],
        "depth": [1],
        "type": [".md", ".html", ".astro"],
        "save_path": "src/pages/${filename}",
        "scaffold": "scaffolds/page.md",
        "excludes": []
    },
    "configs": {
        "path": ["src"],
        "depth": [1],
        "type": [".ts", ".yml"]
    }
}
