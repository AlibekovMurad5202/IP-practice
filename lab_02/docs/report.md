# Отчёт по лабораторной работе №2 по теме "Типы шума на изображении, моделирование аддитивного шума, алгоритмы фильтрации изображений"

## Введение
Перед нами стояли 3 основные задачи, требовавшие выполнения:
* реализация генерации шума на изображении
* реализация шумоподавляющих фильтров:  фильтр "___Гаусса___" и фильтр "___средней точки___"
* замеры времени и качества обработки


## Теоретическая информация

### _Рассмотим генерацию шума с __гауссовым__ распределением._

__Нормальное распределение__ или __распределение Гаусса__ - распределение вероятностей, в одномерном случае задающееся функцией плотности распределения, совпадающей с __функцией Гаусса__:

<a href="https://www.codecogs.com/eqnedit.php?latex=f(x)&space;=&space;\frac{1}{\sigma\sqrt{2\pi}}e^{-\frac{1}{2}(\frac{x&space;-&space;\mu}{\sigma})^{2}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f(x)&space;=&space;\frac{1}{\sigma\sqrt{2\pi}}e^{-\frac{1}{2}(\frac{x&space;-&space;\mu}{\sigma})^{2}}" title="f(x) = \frac{1}{\sigma\sqrt{2\pi}}e^{-\frac{1}{2}(\frac{x - \mu}{\sigma})^{2}}" /></a>

Для генерации шума с __нормальным распределением__ мы использовали __преобразование Бокса-Мюлера__, которое с помощью двух независимых наборов __равномерно распределенных__ чисел позволяет получить два независимых набора __нормально распределенных чисел__. В реализации метода мы использовали следующие формулы:

<a href="https://www.codecogs.com/eqnedit.php?latex=Z_{0}=\sqrt{-2\ln{U_{1}}}cos{(2\pi&space;U_{2})}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Z_{0}=\sqrt{-2\ln{U_{1}}}cos{(2\pi&space;U_{2})}" title="Z_{0}=\sqrt{-2\ln{U_{1}}}cos{(2\pi U_{2})}" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=Z_{1}=\sqrt{-2\ln{U_{1}}}sin{(2\pi&space;U_{2})}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Z_{1}=\sqrt{-2\ln{U_{1}}}sin{(2\pi&space;U_{2})}" title="Z_{1}=\sqrt{-2\ln{U_{1}}}sin{(2\pi U_{2})}" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=where&space;\&space;U_{1},U_{2}\&space;-&space;uniform\&space;distribution" target="_blank"><img src="https://latex.codecogs.com/gif.latex?where&space;\&space;U_{1},U_{2}\&space;-&space;uniform\&space;distribution" title="where \ U_{1},U_{2}\ - uniform\ distribution" /></a> 

<a href="https://www.codecogs.com/eqnedit.php?latex=Z_{1},Z_{2}\&space;-&space;normal\&space;distribution" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Z_{1},Z_{2}\&space;-&space;normal\&space;distribution" title="Z_{1},Z_{2}\ - normal\ distribution" /></a>

### _Рассмотим __фильтр Гаусса__._

__Фильтр Гаусса__ - матричный фильтр, применяющий к окрестности пиксела __распределение Гаусса__. Таким образом, в отличие от фильтра __Усреднение__, пикселы, находящиеся ближе к центру, больше влияют на результирующий цвет, чем дальние.

Матрица __фильтра Гаусса__:

<a href="https://www.codecogs.com/eqnedit.php?latex=G&space;=&space;\frac{1}{\sum_{i&space;=&space;-radius}^{radius}\sum_{j&space;=&space;-radius}^{radius}(g_{ij})}&space;\begin{bmatrix}&space;e^{-\frac{1}{2}\frac{(-radius)^2&space;&plus;&space;(-radius)^2}{\sigma^{2}}}&&space;...&&space;e^{-\frac{1}{2}\frac{(-radius)^2&space;&plus;&space;radius^2}{\sigma^{2}}}\\&space;...&&space;1&&space;...\\&space;e^{-\frac{1}{2}\frac{radius^2&space;&plus;&space;(-radius)^2}{\sigma^{2}}}&&space;...&&space;e^{-\frac{1}{2}\frac{radius^2&space;&plus;&space;radius^2}{\sigma^{2}}}\\&space;\end{bmatrix}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?G&space;=&space;\frac{1}{\sum_{i&space;=&space;-radius}^{radius}\sum_{j&space;=&space;-radius}^{radius}(g_{ij})}&space;\begin{bmatrix}&space;e^{-\frac{1}{2}\frac{(-radius)^2&space;&plus;&space;(-radius)^2}{\sigma^{2}}}&&space;...&&space;e^{-\frac{1}{2}\frac{(-radius)^2&space;&plus;&space;radius^2}{\sigma^{2}}}\\&space;...&&space;1&&space;...\\&space;e^{-\frac{1}{2}\frac{radius^2&space;&plus;&space;(-radius)^2}{\sigma^{2}}}&&space;...&&space;e^{-\frac{1}{2}\frac{radius^2&space;&plus;&space;radius^2}{\sigma^{2}}}\\&space;\end{bmatrix}" title="G = \frac{1}{\sum_{i = -radius}^{radius}\sum_{j = -radius}^{radius}(g_{ij})} \begin{bmatrix} e^{-\frac{1}{2}\frac{(-radius)^2 + (-radius)^2}{\sigma^{2}}}& ...& e^{-\frac{1}{2}\frac{(-radius)^2 + radius^2}{\sigma^{2}}}\\ ...& 1& ...\\ e^{-\frac{1}{2}\frac{radius^2 + (-radius)^2}{\sigma^{2}}}& ...& e^{-\frac{1}{2}\frac{radius^2 + radius^2}{\sigma^{2}}}\\ \end{bmatrix}" /></a>

### _Рассмотим __фильтр средней точки__._

Фильтр средней точки определяет цвет текущего пиксела как среднее между цветами пикселей с максимальной и минимальной яркостью в его окрестности:

<a href="https://www.codecogs.com/eqnedit.php?latex=C&space;=&space;\frac{{}C_{max}&space;&plus;&space;C_{min}}{2}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?C&space;=&space;\frac{{}C_{max}&space;&plus;&space;C_{min}}{2}" title="C = \frac{{}C_{max} + C_{min}}{2}" /></a>

### _Рассмотим вычисление яркости в цветовой модели __BGR__._

Для вычисления яркости для фильтра средней точки мы взяли формулу:

<a href="https://www.codecogs.com/eqnedit.php?latex=Y&space;=&space;0.11&space;*&space;R&space;&plus;&space;0.59&space;*&space;G&space;&plus;&space;0.3&space;*&space;B" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Y&space;=&space;0.11&space;*&space;R&space;&plus;&space;0.59&space;*&space;G&space;&plus;&space;0.3&space;*&space;B" title="Y = 0.11 * R + 0.59 * G + 0.3 * B" /></a>

### _Рассмотрим метрику ___PSNR___._
Предположим мы сравниваем 2 изображения (_X_ и _Y_) с одинаковыми высотой (_H_) и шириной (_W_).
Сначала найдём ___MSE___:

<a href="https://www.codecogs.com/eqnedit.php?latex=MSE&space;=&space;\frac{1}{3HW}&space;\sum\limits_{i=1}^{H}&space;\sum\limits_{j=1}^{W}&space;\|x_{ij}&space;-&space;y_{ij}\|^2&space;\&space;,&space;\\&space;where&space;\&space;\&space;x_{ij}&space;=&space;(B_x,&space;G_x,&space;R_x)^T,&space;\&space;y_{ij}&space;=&space;(B_y,&space;G_y,&space;R_y)^T" target="_blank"><img src="https://latex.codecogs.com/gif.latex?MSE&space;=&space;\frac{1}{3HW}&space;\sum\limits_{i=1}^{H}&space;\sum\limits_{j=1}^{W}&space;\|x_{ij}&space;-&space;y_{ij}\|^2&space;\&space;,&space;\\&space;where&space;\&space;\&space;x_{ij}&space;=&space;(B_x,&space;G_x,&space;R_x)^T,&space;\&space;y_{ij}&space;=&space;(B_y,&space;G_y,&space;R_y)^T" title="MSE = \frac{1}{3HW} \sum\limits_{i=1}^{H} \sum\limits_{j=1}^{W} \|x_{ij} - y_{ij}\|^2 \ , \\ where \ \ x_{ij} = (B_x, G_x, R_x)^T, \ y_{ij} = (B_y, G_y, R_y)^T" /></a>

Теперь найдём ___PSNR___ (_M_ - максимальное значение, т.е. _M_ = 255, т.к. 8-битное изображение):


<a href="https://www.codecogs.com/eqnedit.php?latex=PSNR&space;=&space;10\lg\frac{M^2}{MSE}&space;\\" target="_blank"><img src="https://latex.codecogs.com/gif.latex?PSNR&space;=&space;10\lg\frac{M^2}{MSE}&space;\\" title="PSNR = 10\lg\frac{M^2}{MSE} \\" /></a>

## Результаты замеров качества и времени выполнения
### Результаты генерации шума с __гауссовским распределением__
Время генерации шума: _1.2071290034444475_ с

Сравнение оригинального и зашумленного изображений:

* __MSE__ метрика: _229.6138916015625_

* __PSNR__ метрика: _24.520822016045155_

### Результаты применения __фильтра Гаусса__ к зашумленному изображению
Время применения фильтра нашей реализации: _11.814292492418168_ с

Сравнение зашумленного изображения и результата:

* __MSE__ метрика: _82.55928802490234_

* __PSNR__ метрика: _28.963144218390067_

Время применения фильтра OpenCV реализации: _0.0006952822271095727_ с

Сравнение зашумленного изображения и результата:

* __MSE__ метрика: _86.38785552978516_

* __PSNR__ метрика: _28.76627667545423_

### Результаты применения __фильтра средней точки__ к зашумленному изображению
Время применения фильтра нашей реализации: _6.384115132402732_ с

Сравнение зашумленного изображения и результата:

* __MSE__ метрика: _253.5613250732422_

* __PSNR__ метрика: _24.089973482045806_

## Выводы
В ходе выполнения лабораторной работы нами были изучены основние идеи, лежащие в основе генерации шума изображений и способов борьбы с шумом, на примере реализации генератора шума с __распределением Гаусса__, "__фильтра Гаусса__" и "__фильтра средней точки__". 

Также были проведены замеры времени генерации шума изображения с __распределением Гаусса__ и отличий зашумленного изображения от оригинала. Были проведены замеры времени выполнения и сравнения зашумленного изображения и результата для фильтров "__Гаусса__" и "__средней точки__".

После проведения сравнения изображений, полученных применением "__фильтра Гаусса__" к зашумленным изображениям, удалось выяснить, что наша реализация алгоритма, несмотря на значительную разницу во времени, показывает сравнимые с реализацией OpenCV результаты.
