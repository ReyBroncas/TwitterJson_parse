# TwitterJson parsere

A simple python module to view .json files.

### Run Examples

Module searches tweets using Twitter API by default, however you can view your own .json file. In order to
do this put your file in cache/ and when program asks a query, type the name of your .json file.

```sh
$ python3 main.py
Enter a search query: python
├── [0|str] ──── created_at
├── [1|int] ──── id
├── [2|str] ──── id_str
├── [3|str] ──── text
├── [4|bool] ──── truncated
├── [5|dict] ──── entities
├── [6|dict] ──── metadata
├── [7|str] ──── source
├── [8|NoneType] ──── in_reply_to_status_id
├── [9|NoneType] ──── in_reply_to_status_id_str
├── [10|NoneType] ──── in_reply_to_user_id
├── [11|NoneType] ──── in_reply_to_user_id_str
├── [12|NoneType] ──── in_reply_to_screen_name
├── [13|dict] ──── user
├── [14|NoneType] ──── geo
├── [15|NoneType] ──── coordinates
├── [16|NoneType] ──── place
├── [17|NoneType] ──── contributors
├── [18|dict] ──── retweeted_status
├── [19|bool] ──── is_quote_status
├── [20|int] ──── retweet_count
├── [21|int] ──── favorite_count
├── [22|bool] ──── favorited
├── [23|bool] ──── retweeted
├── [24|bool] ──── possibly_sensitive
├── [25|str] ──── lang
```

### Run Examples
***
![Result:]()
***
