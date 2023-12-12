from myweather import MyLocalWeather

if __name__ == '__main__':
    api_key = '91cbd0452cfe73377852f642ccb1c743'     #your API Key here as string
    loc_weather = MyLocalWeather(api_key)
    loc_weather.create_owm()
    loc_weather.get_ip()
    loc_weather.get_location()
    loc_weather.get_current_weather()
    loc_weather.print_weather()
    print(loc_weather.my_overview)
    match loc_weather.my_overview:
        case 'clear sky':
            led.color(1,0.8,0.2)
        case 'few clouds':
            led.color(0.3,1,1)
        case 'scattered clouds':
            led.color(0.2,0.5,1)
        case 'broken clouds':
            led.color(0,0.2,1)
        case 'shower rain':
            led.color(0,1,0.5)
        case 'rain':
            led.color(0,0.5,0)
        case 'thunderstorm':
            led.color(0,0.5,0.5)
        case 'snow':
            led.color(0.5,0,1)
        case 'mist':
            led.color(0.5,0.5,0.5)
        case _:
            led.color = (1,0,0)