Спершу можна написати два модулі:
- files
- mysql

Цього вистачить для демонстрації та я зміг би вже це використовувати.
Давай почнемо з файлів…

$ thoth config
> Choose archiving method:
> 1) LZ4
> 2) LZMA
> 3) ZIP
> Your choice: 2

> Choose encryption method:
> 1) ChaCha20-Poly1305
> 2) ZIP AES-256 Encryption (неактивна опція через вибір LZMA)
> Your choice: 1

$ thoth config --archive=lzma --encryption=chachapoly
$ thoth config --archive=LZMA --encryption="ChaCha20-Poly1305"
$ thoth config --archive=LZ4 --encryption="ChaCha20-Poly1305"
$ thoth config --archive=lz4 --encryption=aes — використовуватиме LZ4 для архівування і ZIP AES-256 якщо випадок із шифруванням
$ thoth config --archive=LZ4 --encryption="ZIP AES-256"


$ thoth files backup /path/to/file — робить резервну копію файлу (при першому запуску нагадує що треба зробити налаштування)
$ thoth files backup /path/to/file --archive=lzma --encryption=chachapoly — робить резервну копію файлу із архівом LZMA та шивруванням ChaCha20-Poly1305
$ thoth files backup /path/to/file --encryption=aes — робить резервну копію файлу із архівом ZIP та шивруванням AES-256
$ thoth files backup /path/to/file --archive=lz4 --encryption=aes — поверне помилку, несумісні алгоритми

$ thoth files backup /path/to/file --armor — робить резервну копію файлу і шифрує його (повертає id бекапу)
$ thoth files backup /path/to/directуry/ — робить резервну копію директорії (повертає id бекапу)

$ thoth files restore /path/to/file — відновлює резервну копію файлу
$ thoth files restore /path/to/directory/ — відновлює останню резервну копію директорії
$ thoth files restore -i /path/to/directory/ — інтерактивний режим, запитує яку версію резервної копії відновити

$ thoth files restore /path/to/directory/ — відновлює останню резервну копію директорії
$ thoth files restore /path/to/directory/ 74d624d — відновлює певну версію директорії (74d624d це фрагмент SHA-256 суми)

$ thoth files list /path/to/directory/ — виводить список усіх бекапів за запланованих задач по директорії

$ thoth files list — виводить список усіх директорій із бекапами, разом із їх статистикою

$ thoth files backup /path/to/file/or/directory/ --cron="0 2 * * *" — ставить бекап директорії щодня о 2 ночі (повертає cron-id)
$ thoth files restore /path/to/file/or/directory/ --cron="0 2 * * *" — ставить відновлення останньої версії директорії щодня о 2 ночі (повертає cron-id)
$ thoth files restore /path/to/file/or/directory/ 74d624d --cron="0 2 * * *" — ставить відновлення певної версії директорії щодня о 2 ночі (повертає cron-id)

$ thoth files cp 74d624d ./ — скопіювати архів бекапу 74d624d в поточну директорію
$ thoth files cp 74d624d ./ --pack — скопіювати архів бекапу 74d624d в поточну директорію
$ thoth files cp 74d624d ./ --unpack — скопіювати файли з бекапу 74d624d в поточну директорію

$ thoth cron list — виводить список усіх запланованих задач
$ thoth cron — те ж саме що "thoth cron list"
$ thoth cron rm 40fb488 — видаляє запланований бекап
$ thoth cron stop 40fb488 — зупиняє запланований бекап
$ thoth cron start 40fb488 — запускау запланований бекап
$ thoth cron status 40fb488 — виводить статус запланового бекапу

$ thoth mysql backup myDb — зробити бекап бази myDb
$ thoth mysql backup myDb --cron="0 2 * * 1" — робити бекап щопонеділка о 2:00
$ thoth mysql restore myDb — відновити бекап бази myDb
$ thoth mysql restore myDb -i — інтерактивний режим, буде запитувати
$ thoth mysql list myDb — вивести список усіх бекапів і запланованих задач із їх статусами
$ thoth files rm 74d624d — видалити певний бекап

$ thoth chain create myChain
$ thoth chain create myOtherChain
$ thoth chain use
$ thoth chain use myChain
$ thoth chain list
$ thoth chain drop
$ thoth chain add /some/file /some/dir/
$ thoth chain rm /some/file
$ thoth chain show
$ thoth chain edit
$ thoth chain backup
$ thoth chain backup --archive=lz4 --encryption
$ thoth chain restore
$ thoth chain restore -i
