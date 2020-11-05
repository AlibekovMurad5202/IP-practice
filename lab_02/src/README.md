# Инструкция к запуску демо
```bash
python <name>_demo.py
```
### Обязательные параметры:
* `-i / --input` - путь до изображения

### Опциональные параметры:
* `-m / --mean` - математическое ожидание (среднее значение) нормального распределения (_по умолчанию_ равно 0)
* `-s / --sigma` - среднеквадратическое отклонение нормального распределения (_по умолчанию_ равно 20)
* `-r / --radius` - радиус ядра матричного фильтра (_по умолчанию_ равен 3) (присутствует в gauss_denoising_demo и midpoint_filter_denoising_demo)

## Демонстрация запуска демо
### Запуск gauss_noise_demo.py
<img src="../resources/gauss_noise_demo_record.gif" width="850" height="500" />

### Запуск gauss_denoising_demo.py
<img src="../resources/gauss_denoising_demo_record.gif" width="850" height="500" />

### Запуск midpoint_filter_denoising_demo.py
<img src="../resources/midpoint_filter_denoising_demo_record.gif" width="850" height="500" />