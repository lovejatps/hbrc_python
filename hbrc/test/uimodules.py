'''
Created on 2016年9月20日
coding=utf-8
@author: huxiaoning
'''
import tornado


class Entry(tornado.web.UIModule):
    def render(self, entry, show_comments=False):
        return self.render_string("module-entry.html",entry=entry,show_comments=show_comments)
