#This config is not fully complete...

# load autoconfig.yml
config.load_autoconfig()

c.backend = 'webengine'

# statusbar
c.statusbar.padding = {'bottom': 3, 'left': 2, 'right': 2, 'top': 3}
c.statusbar.hide = True

# scrolling
c.scrolling.bar = True
c.scrolling.smooth = True
c.completion.scrollbar.width = 8

# tabs
c.tabs.favicons.show= False
c.tabs.width.indicator = 0
c.tabs.title.alignment = 'center'
c.tabs.padding = {'bottom': 6, 'left': 16, 'right': 16, 'top': 6}

# downloads
c.downloads.location.directory = '~/Downloads'

# downloads bar
c.colors.downloads.bar.bg = '#478061'


# content
c.content.plugins = True

# colors
c.colors.completion.fg = '#EEF6F6'
c.colors.completion.odd.bg = '#232323'
c.colors.completion.even.bg = c.colors.completion.odd.bg
c.colors.completion.category.fg = '#478061'
c.colors.completion.category.bg = '#282828'
c.colors.completion.category.border.top = '#282828'
c.colors.completion.category.border.bottom = c.colors.completion.category.border.top 
c.colors.completion.item.selected.fg = '#282828'
c.colors.completion.item.selected.bg = '#fe8019'
c.colors.completion.item.selected.border.top = '#fe8019'
c.colors.completion.item.selected.border.bottom = c.colors.completion.item.selected.border.top
c.colors.completion.match.fg = '#fe8019'

c.colors.statusbar.normal.fg = '#EEF6F6'
c.colors.statusbar.normal.bg = '#478061'
c.colors.statusbar.command.fg = c.colors.statusbar.normal.fg
c.colors.statusbar.command.bg = c.colors.statusbar.normal.bg

c.colors.tabs.odd.fg = '#EEF6F6'
c.colors.tabs.odd.bg = '#232323'
c.colors.tabs.even.fg = c.colors.tabs.odd.fg
c.colors.tabs.even.bg = c.colors.tabs.odd.bg
c.colors.tabs.selected.odd.fg = '#EEF6F6'
c.colors.tabs.selected.odd.bg = '#478061'
c.colors.tabs.selected.even.fg = c.colors.tabs.selected.odd.fg
c.colors.tabs.selected.even.bg = c.colors.tabs.selected.odd.bg

c.colors.downloads.bar.bg = '#32302f'

# fonts
c.fonts.monospace = '"terminus"'
c.fonts.completion.category = '10pt monospace'
c.fonts.completion.entry = '10pt monospace'
c.fonts.tabs = '10pt monospace'
c.fonts.statusbar = '10pt monospace'
c.fonts.downloads = '10pt monospace'
c.fonts.debug_console = '10pt monospace'
c.fonts.keyhint = '10pt monospace'
c.fonts.messages.error = '10pt monospace'
c.fonts.messages.info = '10pt monospace'
c.fonts.messages.warning = '10pt monospace'

c.fonts.hints = 'bold 12px DejaVu Sans Mono'
c.fonts.web.family.standard = 'DejaVu Sans'
c.fonts.web.family.fixed = 'DejaVu Sans Mono'
c.fonts.web.family.serif = 'DejaVu Serif'
c.fonts.web.family.sans_serif = 'DejaVu Sans'

# keybindings
config.bind('K', 'tab-next')
config.bind('J', 'tab-prev')
config.bind('Q', 'tab-close')
config.unbind('F')
config.bind('F', 'search')
