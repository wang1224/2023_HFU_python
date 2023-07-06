# 天氣太熱而且下雨天，就請假不去上課
# 國定假日或是颱風天，就請假不去上課
# 心情不好而且下雨天，就請假不去上課

is_hot = True
is_raining = True
is_holiday = True
is_typhoon = True
is_emotional = True

is_school = True

if is_hot and is_raining:
    is_school = False
if is_holiday or is_typhoon:
    is_school = False
if is_emotional and is_raining:
    is_school = False

# refactor
if (is_raining and (is_hot or is_emotional)) or \
    is_holiday or is_typhoon:
    is_school = False
