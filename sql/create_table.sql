CREATE TABLE IF NOT EXISTS f_artist(
	artist_id SERIAL,
	artist_name TEXT,
	artist_location TEXT,
	artist_longitude TEXT,
	artist_latitude TEXT,
	PRIMARY KEY (artist_id)
);

CREATE TABLE IF NOT EXISTS f_song (
	song_id SERIAL, 
	song_name TEXT,
	year INT,
	length INT,
	artist_id INT references f_artist(artist_id),
	PRIMARY KEY (song_id)
);
