def get_en_youbi(ja):
    day_of_weeks = {'日':'Sunday', '月':'Monday', '火':'Tuesday', '水':'Wednesday',
                    '木':'Thursday', '金':'Friday', '土':'Saturday'}
    if ja not in day_of_weeks:
        return None
    return day_of_weeks[ja]

print(get_en_youbi('水'))
    