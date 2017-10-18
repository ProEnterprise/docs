"""
Configuration for docs
"""

source_link = "https://github.com/ProEnterprise/docs.git"
docs_base_url = "https://enterprise.plus.co.zm/docs"
headline = "Documentation"
sub_heading = "Pro Enteprise documentation"

def get_context(context):
        context.brand_html = "Pro Enterprise"
        context.favicon = 'https://enterprise.plus.co.zm/files/favicon-32x32.png'
        context.top_bar_items = [
                {"label": "About", "url": context.docs_base_url + "/about"},
		{"label": "Product", "url": context.docs_base_url + "/all-item-groups/products"},
		{"label": "Blog", "url": context.docs_base_url + "/blog"},
		{"label": "Contact", "url": context.docs_base_url + "/contact"}
	]

pass
