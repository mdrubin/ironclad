
def _ironclad_getter(self):
    return self._dispatcher.ic_getter_method('{1}{0}', self, IntPtr({2}))
_ironclad_class_attrs['{0}'] = _ironclad_getter
