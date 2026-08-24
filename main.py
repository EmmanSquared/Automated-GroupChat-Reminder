import core

bool_node = True
first_pass = True

while bool_node:
    if core.one_hour_before.chat_time > core.datetime.now():
        print(f'{core.datetime.now()} Minutes left before reminding: {round(core.one_hour_before.timeleft_till_next_reminder/60)}.')
        print('at 1 hour')
        core.sleep(core.one_hour_before.timeleft_till_next_reminder)
        if first_pass:
            first_pass = False
            continue
        core.window_tasks()
        first_pass = True

    elif core.fifteen_mins_before.chat_time > core.datetime.now():
        print(f'{core.datetime.now()} Minutes left before reminding: {round(core.fifteen_mins_before.timeleft_till_next_reminder/60)}.')
        print('at 15 mins')
        core.sleep(core.fifteen_mins_before.timeleft_till_next_reminder)
        if first_pass:
            first_pass = False
            continue
        core.window_tasks()
        first_pass = True

    elif core.meet_reminder.chat_time > core.datetime.now():
        print(f'{core.datetime.now()} Minutes left before reminding: {round(core.fifteen_mins_before.timeleft_till_next_reminder/60)}.')
        print('at 0 mins')
        core.sleep(core.meet_reminder.timeleft_till_next_reminder)
        if first_pass:
            first_pass = False
            continue
        core.window_tasks()

    else:
        print('Time for meet had already passed.')
        bool_node = False