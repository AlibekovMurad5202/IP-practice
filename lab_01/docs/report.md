# Отчёт по лабораторной работе №1 по теме "Точечные фильтры"

## Введение
Перед нами стояли 3 основные задачи, требовавшие выполнения:
* реализация прямого/обратного перевода между цветовыми моделями
* реализация фильтра "___Увеличение яркости___" для разных цветовых моделей
* замеры времени и качества обработки

## Теоретическая информация
В качестве цветовых моделей мы взяли ___BGR ⇆ YCrCb___, а в качестве метрики сходства - ___PSNR___
### _Рассмотим перевод изображения из цветовой модели __BGR__ в цветовую модель __Grayscale__._
Для перевода в __Grayscale__ мы взяли формулу luminosity:

<a href="https://www.codecogs.com/eqnedit.php?latex=Y&space;=&space;0.21&space;*&space;R&space;&plus;&space;0.72&space;*&space;G&space;&plus;&space;0.07&space;*&space;B" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Y&space;=&space;0.21&space;*&space;R&space;&plus;&space;0.72&space;*&space;G&space;&plus;&space;0.07&space;*&space;B" title="Y = 0.21 * R + 0.72 * G + 0.07 * B" /></a>

В __OpenCV__ используется другая формула:

<a href="https://www.codecogs.com/eqnedit.php?latex=Y&space;=&space;0.299&space;R&space;&plus;&space;0.587&space;G&space;&plus;&space;0.114&space;B" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Y&space;=&space;0.299&space;R&space;&plus;&space;0.587&space;G&space;&plus;&space;0.114&space;B" title="Y = 0.299 R + 0.587 G + 0.114 B" /></a>

Всвязи с различиями в формулах, можем сделать вывод, что при преобразовании средствами OpenCV зелёный цвет будет преобразован в более светлый оттенок серого, чем при преобразовании при помощи формулы luminosity. Синий и красный цвета, в свою очередь будут преобразованы в более тёмные оттенки серого.
### _Рассмотим прямой/обратный перевод изображения из цветовой модели __BGR__ в цветовую модель __YCrCb__._
__YCrCb__ - цветовое пространство, которое используется для передачи цветных изображений в компонентном видео и цифровой фотографии.
__Y__ — компонента яркости, __Cr__ и __Cb__ являются красной и синей цветоразностными компонентами соответсвенно.

Для переводов используют следующие формулы преобразования (_delta_ = 128, т.к. работаем с 8-битными изображениями):

* ___RGB ⟶ YCrCb___:


<a href="https://www.codecogs.com/eqnedit.php?latex=\left\{&space;\begin{array}{ll}&space;Y&space;=&space;0.299&space;*&space;R&space;&plus;&space;0.587&space;*&space;G&space;&plus;&space;0.114&space;*&space;B&space;\\&space;Cr&space;=&space;(R&space;-&space;Y)&space;*&space;0.713&space;\&space;&plus;&space;\&space;delta&space;\\&space;Cb&space;=&space;(B&space;-&space;Y)&space;*&space;0.564&space;\&space;&plus;&space;\&space;delta&space;\\&space;\end{array}&space;\right." target="_blank"><img src="https://latex.codecogs.com/gif.latex?\left\{&space;\begin{array}{ll}&space;Y&space;=&space;0.299&space;*&space;R&space;&plus;&space;0.587&space;*&space;G&space;&plus;&space;0.114&space;*&space;B&space;\\&space;Cr&space;=&space;(R&space;-&space;Y)&space;*&space;0.713&space;\&space;&plus;&space;\&space;delta&space;\\&space;Cb&space;=&space;(B&space;-&space;Y)&space;*&space;0.564&space;\&space;&plus;&space;\&space;delta&space;\\&space;\end{array}&space;\right." title="\left\{ \begin{array}{ll} Y = 0.299 * R + 0.587 * G + 0.114 * B \\ Cr = (R - Y) * 0.713 \ + \ delta \\ Cb = (B - Y) * 0.564 \ + \ delta \\ \end{array} \right." /></a>

* ___YCrCb ⟶ RGB___:


<a href="https://www.codecogs.com/eqnedit.php?latex=\left\{&space;\begin{array}{ll}&space;R&space;=&space;Y&space;&plus;&space;1.403&space;*&space;(Cr&space;-&space;delta)&space;\\&space;G&space;=&space;Y&space;-&space;0.714&space;*&space;(Cr&space;-&space;delta)&space;-&space;0.344&space;*&space;(Cb&space;-&space;delta)&space;\\&space;B&space;=&space;Y&space;&plus;&space;1.773&space;*&space;(Cb&space;-&space;delta)&space;\\&space;\end{array}&space;\right." target="_blank"><img src="https://latex.codecogs.com/gif.latex?\left\{&space;\begin{array}{ll}&space;R&space;=&space;Y&space;&plus;&space;1.403&space;*&space;(Cr&space;-&space;delta)&space;\\&space;G&space;=&space;Y&space;-&space;0.714&space;*&space;(Cr&space;-&space;delta)&space;-&space;0.344&space;*&space;(Cb&space;-&space;delta)&space;\\&space;B&space;=&space;Y&space;&plus;&space;1.773&space;*&space;(Cb&space;-&space;delta)&space;\\&space;\end{array}&space;\right." title="\left\{ \begin{array}{ll} R = Y + 1.403 * (Cr - delta) \\ G = Y - 0.714 * (Cr - delta) - 0.344 * (Cb - delta) \\ B = Y + 1.773 * (Cb - delta) \\ \end{array} \right." /></a>

### _Рассмотрим фильтр "___Увеличение яркости___"._
Это __точечный__ фильтр, поэтому операция, лежащая в его основе, применяется к каждому пискелю. Само правило фильтрации зависит от выбора цветовой модели изображения:

* для цветовой модели __BGR__ в качестве правила фильтрации было взято следующее преобразование (_С_ = _const_):


<a href="https://www.codecogs.com/eqnedit.php?latex=\left\{&space;\begin{array}{ll}&space;R'&space;=&space;\max\{\min\{R&space;&plus;&space;C,&space;\&space;255\},&space;\&space;0\}&space;\\&space;G'&space;=&space;\max\{\min\{G&space;&plus;&space;C,&space;\&space;255\},&space;\&space;0\}&space;\\&space;B'&space;=&space;\max\{\min\{B&space;&plus;&space;C,&space;\&space;255\},&space;\&space;0\}&space;\\&space;\end{array}&space;\right." target="_blank"><img src="https://latex.codecogs.com/gif.latex?\left\{&space;\begin{array}{ll}&space;R'&space;=&space;\max\{\min\{R&space;&plus;&space;C,&space;\&space;255\},&space;\&space;0\}&space;\\&space;G'&space;=&space;\max\{\min\{G&space;&plus;&space;C,&space;\&space;255\},&space;\&space;0\}&space;\\&space;B'&space;=&space;\max\{\min\{B&space;&plus;&space;C,&space;\&space;255\},&space;\&space;0\}&space;\\&space;\end{array}&space;\right." title="\left\{ \begin{array}{ll} R' = \max\{\min\{R + C, \ 255\}, \ 0\} \\ G' = \max\{\min\{G + C, \ 255\}, \ 0\} \\ B' = \max\{\min\{B + C, \ 255\}, \ 0\} \\ \end{array} \right." /></a>

* так как в цветовой модели __YCrCb__ компонента __Y__ отвечает за яркость, то достаточно увеличить только её оставив две другие неизменными, и тогда в качестве правила фильтрации можно взять следующее преобразование ($С = const$):


<a href="https://www.codecogs.com/eqnedit.php?latex=\left\{&space;\begin{array}{ll}&space;Y'&space;=&space;\max\{\min\{Y&space;&plus;&space;C,&space;\&space;255\},&space;\&space;0\}&space;\\&space;Cr'&space;=&space;Cr&space;\\&space;Cb'&space;=&space;Cb&space;\\&space;\end{array}&space;\right." target="_blank"><img src="https://latex.codecogs.com/gif.latex?\left\{&space;\begin{array}{ll}&space;Y'&space;=&space;\max\{\min\{Y&space;&plus;&space;C,&space;\&space;255\},&space;\&space;0\}&space;\\&space;Cr'&space;=&space;Cr&space;\\&space;Cb'&space;=&space;Cb&space;\\&space;\end{array}&space;\right." title="\left\{ \begin{array}{ll} Y' = \max\{\min\{Y + C, \ 255\}, \ 0\} \\ Cr' = Cr \\ Cb' = Cb \\ \end{array} \right." /></a>

На основе формул преобразования можно сделать вывод, что применение фильтра "___Увеличение яркости___" к изображению в цветовой модели __YCrCb__ будет выполняться в 3 раза быстрее, чем применение фильтра к тому же изображению в __BGR__ представлении.

### _Рассмотрим метрику ___PSNR___._
Предположим мы сравниваем 2 изображения (_X_ и _Y_) с одинаковыми высотой (_H_) и шириной (_W_).
Сначала найдём ___MSE___:

<a href="https://www.codecogs.com/eqnedit.php?latex=MSE&space;=&space;\frac{1}{3HW}&space;\sum\limits_{i=1}^{H}&space;\sum\limits_{j=1}^{W}&space;\|x_{ij}&space;-&space;y_{ij}\|^2&space;\&space;,&space;\\&space;where&space;\&space;\&space;x_{ij}&space;=&space;(B_x,&space;G_x,&space;R_x)^T,&space;\&space;y_{ij}&space;=&space;(B_y,&space;G_y,&space;R_y)^T" target="_blank"><img src="https://latex.codecogs.com/gif.latex?MSE&space;=&space;\frac{1}{3HW}&space;\sum\limits_{i=1}^{H}&space;\sum\limits_{j=1}^{W}&space;\|x_{ij}&space;-&space;y_{ij}\|^2&space;\&space;,&space;\\&space;where&space;\&space;\&space;x_{ij}&space;=&space;(B_x,&space;G_x,&space;R_x)^T,&space;\&space;y_{ij}&space;=&space;(B_y,&space;G_y,&space;R_y)^T" title="MSE = \frac{1}{3HW} \sum\limits_{i=1}^{H} \sum\limits_{j=1}^{W} \|x_{ij} - y_{ij}\|^2 \ , \\ where \ \ x_{ij} = (B_x, G_x, R_x)^T, \ y_{ij} = (B_y, G_y, R_y)^T" /></a>

Теперь найдём ___PSNR___ (_M_ - максимальное значение, т.е. _M_ = 255, т.к. 8-битное изображение):


<a href="https://www.codecogs.com/eqnedit.php?latex=PSNR&space;=&space;10\lg\frac{M^2}{MSE}&space;\\" target="_blank"><img src="https://latex.codecogs.com/gif.latex?PSNR&space;=&space;10\lg\frac{M^2}{MSE}&space;\\" title="PSNR = 10\lg\frac{M^2}{MSE} \\" /></a>

## Результаты замеров качества и времени выполнения

### Результаты применения фильтра повышения яркости в разных цветовых моделях
Время применения фильтра яркости в __BGR__ модели: _0.8774815570303219_ с

Время применения фильтра яркости в __YCrCb__ модели: _0.2160099375180895_ с

Результаты сравнения полученных изображений в цветовой модели __BGR__:

* __MSE__ метрика: _100.48059844970703_

* __PSNR__ метрика: _28.109981478642055_

### Результаты преобразований из __BGR__ модели в __Grayscale__
Время применения преобразования из _BGR_ модели в __Grayscale__ cредствами OpenCV: _0.0758409675497243_ с

Время применения преобразования из _BGR_ модели в __Grayscale__ реализованным алгоритмом: _0.039901741438488236_ с

* __MSE__ метрика: _23.270584106445312_

* __PSNR__ метрика: _34.46273076376955_

### Результаты преобразований из __BGR__ модели в __YCrCb__ и обратно

1. __BGR__ -> __YCrCb__ средствами OpenCV, __YCrCb__ -> __BGR__ также средствами OpenCV

    * __MSE__ метрика: _0.1223297119140625_

    * __PSNR__ метрика: _57.25548407894222_

2. __BGR__ -> __YCrCb__ реализованным алгоритмом, __YCrCb__ -> __BGR__ средствами OpenCV

    * __MSE__ метрика: _0.4443766176700592

    * __PSNR__ метрика: _51.65329161823264_

3. __BGR__ -> __YCrCb__ средствами OpenCV, __YCrCb__ -> __BGR__ реализованным алгоритмом

    * __MSE__ метрика: _0.1589762419462204_

    * __PSNR__ метрика: _56.11748134425447_

4. __BGR__ -> __YCrCb__ реализованным алгоритмом, __YCrCb__ -> __BGR__ также реализованным алгоритмом

    * __MSE__ метрика: _0.7757008671760559_

   * __PSNR__ метрика: _49.23386083914423_

## Выводы
В ходе выполнения лабораторной работы нами были изучены основние идеи, 
лежащие в основе точечных фильтров и преобразобаний цветовых моделей, на примере реализации точечного фильтра "__Увеличение яркости__" и прямого/обратного перевода изображения из цветовой модели __BGR__ в цветовую модель __YCrCb__. А также были проведены замеры времени применения точечного фильтра "__Увеличение яркости__" к изображению в различных цветовых пространствах, тем самым подтвердив предположение о 3-х кратном увеличении скорости выполнения при работе с __YCrCb__ представлением изображения.

Сравнение изображений, преобразованных в __Grayscale__ подтвердило предположение о различиях преобразования цветов при помощи формулы luminosity и средствами OpenCV.

Сравнение изображений из разных цветовых моделей после применения фильтров яркости показывает, что эти изображения близки к идентичным. Небольшую разницу между ними можно отнести к округлениям при повышении яркости в __BGR__ модели, в отличие от __YCrCb__ модели, а также к преобразованиям между цветовыми моделями, необходимыми для сравнения результатов.

Было проведено сравнение между алгоритмами конвертации изображения OpenCV и реализованными нами. Реализация OpenCV показала лучшее качество конвертации из одной модели в другую - __PSNR__ для алгоритмов OpenCV выше __PSNR__ для наших алгоритмов на 8 дБ.