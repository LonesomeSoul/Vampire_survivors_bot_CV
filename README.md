# Vampire_survivors_bot_CV
A bot for Vampire Survivors steam game
Геймплей: https://youtu.be/hXyIs59MV2k
Видеоинструкция: https://youtu.be/hXyIs59MV2k
Ссылка для скачивания модели: https://drive.google.com/file/d/1uqH2nk8fMYsAT_FX6DfvaBgkbEp0-07C/view?usp=sharing

Порядок запуска бота:

1) !После выполнения этого шага скрипт создаст папку Vampire_survivors_bot в папке пользователя (C:\Users\User)!

Запустить скрипт Vampire_grab_screen.py для создания конфига 

2)
Если необходимо поменять директорию, в которую будут сохраняться 
скриншоты для обучения модели, нужно вручную указать в файле-конфиге желаемый путь.

3)
Еще раз запустить этот скрипт, если игровая область не соответствует размеру 1920 на 1080.

Чтобы выделить нужную область, нужно два раза нажать ЛКМ в углах игровой области на скриншоте экрана, который выведет скрипт.

Для удаления последней точки - нужно нажать ПКМ.

Чтобы сохранить выделенную область - нужно нажать Escape. Escape завершит работу скрипта.

Желательно, чтобы игровая область была выделена максимально корректно (без черных полей и интерфейса windows)

4)
Если необходимо самому обучить модель - нужно открыть скрипт Vampire_survivors_collect_data_and_train_model.ipynb 

Клетка под областью "ОБУЧЕНИЕ МОДЕЛИ - СБОР ДАННЫХ" отвечает за сбор данных для обучающей выборки. Активировав ее, скрипт будет собирать скриншоты игры и распределять их по папкам, соотвествующим стрелкам, которые были нажаты во время скриншота.

Частоту сбора скриншотов можно регулировать, меняя аргумент функции cv2.waitKey(20) в конце клетки.

После клетки сбора данных идут клетки обучения модели и сохранения ее в папку, указанную ранее в конфиге.

5)
Запуск бота - необходимо скачать модель и поместить ее в папку, которая указана в конфиге, затем открыть игру, выбрать персонажа и карту, (важно оставить курсор на кнопке "Start"). затем запустить скрипт Vampire_bot.py и сделать активным игровое окно.
