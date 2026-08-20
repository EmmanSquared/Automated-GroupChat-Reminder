import core

if core.thirty_mins_before.chat_time > core.datetime.now():
    print(f'Minutes left before reminding: {round(core.thirty_mins_before.timeleft_till_next_reminder)}.')
    core.sleep(core.thirty_mins_before.timeleft_till_next_reminder)
    core.window_tasks()

elif core.ten_mins_before.chat_time > core.meet_reminder.chat_time:
    print(f'Minutes left before reminding: {round(core.ten_mins_before.timeleft_till_next_reminder)}.')
    core.sleep(core.ten_mins_before.timeleft_till_next_reminder)
    core.window_tasks()
    core.sleep(600)
    core.window_tasks()

else:
    print('Time for meet had already passed.')