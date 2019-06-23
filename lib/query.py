query = {}

# log dataset queries

query['user_insert'] = 'insert into d_app_user (first_name, last_name, gender, level) values (%s, %s, %s, %s) on conflict (first_name, last_name) do nothing'

query['timestamp_insert'] = 'insert into d_timestamp (year, month, day, hour, minute, second, weekday, timestamp, user_id) values (%s, %s, %s, %s, %s, %s, %s, %s, (select user_id from d_app_user where first_name = %s and last_name = %s))'

query['songplay_insert'] = 'insert into f_songplay (start_time,user_id, level,song_id,artist_id,session_id) values (%s, (select user_id from d_app_user where first_name = %s and last_name = %s), %s, (select song_id from d_song where song_name = %s and artist_id = (select artist_id from d_artist where artist_name = %s)),(select artist_id from d_artist where artist_name= %s),%s)'

# song dataset queries 

query['artist_insert'] = 'insert into d_artist (artist_id, artist_name, artist_location, artist_longitude, artist_latitude) values (%s, %s, %s, %s, %s) on conflict (artist_id, artist_name) do nothing'

query['song_insert'] = 'insert into d_song (song_id, song_name, year, length, artist_key) values (%s, %s, %s, %s, (select artist_key from d_artist where artist_name=%s)) on conflict (song_name, song_id) do nothing'
