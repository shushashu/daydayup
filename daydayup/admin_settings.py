'''
:autor  heroHu
:time   2019/01/01
'''

SUIT_CONFIG = {
    'ADMIN_NAME': '听雨轩',
    'LIST_PER_PAGE': 20,

    'SHOW_REQUIRED_ASTERISK': True,
    'CONFIRM_UNSAVED_CHANGES': True,

    'MENU': (
        {
            'label': '历史上的今天',
            'app': 'historytoday',
            'models': ('HistoryStory', 'StoryPic')
        },
        {
            'label': '财务管理',
            'app': 'pfp',
            'models': ('MoneyLine', 'GoldList')
        },
        {
            'label': '公司全景',
            'app': 'pfp',
            'models': ('CompanyModel',)
        }
    )
}
