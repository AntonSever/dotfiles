import sublime
import sublime_plugin
import re


class FindPlaceholdersCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        region = sublime.Region(0, self.view.size())
        raw_text = self.view.substr(region)

        pattern = r'{([\w\.]+?)}'
        pattern = re.compile(pattern)
        results = re.findall(pattern, raw_text)
        results = set(results)
        results = '\n'.join(results)

        window = self.view.window()
        scratch = window.new_file()
        scratch.set_scratch(True)
        scratch.run_command('insert', {'characters': results})
