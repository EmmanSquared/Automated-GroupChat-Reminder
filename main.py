import core

bool_node = True

while bool_node:
    if core.afternoon_reminder.chat_time > core.datetime.now():
        print(f'{core.datetime.now()} Minutes left before reminding: {round(core.afternoon_reminder.timeleft_till_next_reminder/60)}.')
        print('at afternoon')
        core.sleep(core.afternoon_reminder.timeleft_till_next_reminder)
        core.window_tasks()

    elif core.one_hour_before.chat_time > core.datetime.now():
        print(f'{core.datetime.now()} Minutes left before reminding: {round(core.one_hour_before.timeleft_till_next_reminder/60)}.')
        print('at 1 hour')
        core.sleep(core.one_hour_before.timeleft_till_next_reminder)
        core.window_tasks()

    elif core.fifteen_mins_before.chat_time > core.datetime.now():
        print(f'{core.datetime.now()} Minutes left before reminding: {round(core.fifteen_mins_before.timeleft_till_next_reminder/60)}.')
        print('at 15 mins')
        core.sleep(core.fifteen_mins_before.timeleft_till_next_reminder)
        core.window_tasks()

    elif core.meet_reminder.chat_time > core.datetime.now():
        print(f'{core.datetime.now()} Minutes left before reminding: {round(core.fifteen_mins_before.timeleft_till_next_reminder/60)}.')
        print('at 0 mins')
        core.sleep(core.meet_reminder.timeleft_till_next_reminder)
        core.window_tasks()

    else:
        print('Time for meet had already passed.')
        bool_node = False