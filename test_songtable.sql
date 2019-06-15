insert into f_songplay (
	start_time,
	user_id, 
	level,
	song_id,
	artist_id,
	session_id
) 

values (
	100000, 
	(select user_id from d_app_user where first_name = 'Kaylee' and 
	last_name = 'Summers'),
	'FREE',
	(select song_id from d_song where song_name = 'You Gotta Be' and artist_id = (
	select artist_id from d_artist where artist_name = 'Des''ree')),
	(select artist_id from d_artist where artist_name= 'Des''ree'),
	251
);

