# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.button import Button

class TestApp(App):
	def build(self):
		return Button(text=u'こんにちは、世界！')

TestApp().run();