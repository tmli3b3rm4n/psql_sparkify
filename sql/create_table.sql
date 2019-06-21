CREATE TABLE IF NOT EXISTS d_artist(
	artist_key SERIAL,
	artist_id TEXT NOT NULL,
	artist_name TEXT NOT NULL,
	artist_location TEXT,
	artist_longitude NUMERIC,
	artist_latitude NUMERIC,
	CONSTRAINT d_artist_pk PRIMARY KEY (artist_key),
	UNIQUE(artist_id)
);

CREATE TABLE IF NOT EXISTS d_song (
	song_key SERIAL,
	song_id TEXT NOT NULL, 
	song_name TEXT NOT NULL,
	year INT,
	length INT,
	artist_id TEXT references d_artist(artist_id),
	CONSTRAINT d_song_pk PRIMARY KEY (song_key),
	UNIQUE (song_id, artist_key)

);

CREATE TABLE IF NOT EXISTS d_app_user (
	user_key SERIAL,
	user_id SERIAL,
	first_name TEXT,
	last_name TEXT,
	gender VARCHAR(1),
	level TEXT,
	PRIMARY KEY (user_key),
	UNIQUE (first_name, last_name)
);

CREATE TABLE IF NOT EXISTS d_timestamp (
	timestamp_key SERIAL,
	second INT,
	minute INT,
	hour INT,
	day INT,
	month INT,
	year INT,
	weekday BOOL,
	timestamp BIGINT,
	user_id INT REFERENCES d_app_user(user_id),
	PRIMARY KEY (timestamp_id)
);

CREATE TABLE IF NOT EXISTS f_songplay (
	songplay_key SERIAL,
	start_time BIGINT,
	user_id INT REFERENCES d_app_user(user_id),
	level TEXT,
	song_id INT REFERENCES d_song(song_id),
	artist_id INT REFERENCES d_artist(artist_id),
	session_id INT,
	PRIMARY KEY (songplay_id)
);