# optimizer.py

from seo import analyze, optimize

class ContentOptimizer:
    def __init__(self, target_keywords):
        self.target_keywords = target_keywords

    def optimize_content(self, title, content):
        seo_analysis = analyze(content)
        optimized_content = optimize(content, keywords=self.target_keywords)
        return title, optimized_content
