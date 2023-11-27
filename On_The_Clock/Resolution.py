from datetime import datetime

def get_hours(shifts):
    def time_to_hours(time_str):
        time_format = "%I:%M%p"
        time = datetime.strptime(time_str, time_format)
        return time.hour + time.minute / 60
    
    result = []
    for times in shifts:
        start_time = time_to_hours(times[0])
        end_time = time_to_hours (times[1])
        
        if end_time < start_time:
            end_time += 24
        
        worked_hours = round(end_time - start_time, 2)
        worked_hours = round(worked_hours*4)/4
        result.append(worked_hours)
    
    return result