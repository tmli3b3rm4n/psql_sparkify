CREATE TABLE IF NOT EXISTS d_artist(
	artist_key SERIAL,
	artist_id TEXT NOT NULL,
	artist_name TEXT NOT NULL,
	artist_location TEXT,
	artist_longitude NUMERIC,
	artist_latitude NUMERIC,
	CONSTRAINT d_artist_pk PRIMARY KEY (artist_key),
	UNIQUE(artist_id, artist_name)
);

CREATE TABLE IF NOT EXISTS d_song (
	song_key SERIAL,
	song_id TEXT NOT NULL, 
	song_name TEXT NOT NULL,
	year INT,
	length INT,
	artist_key INT references d_artist(artist_key),
	CONSTRAINT d_song_pk PRIMARY KEY (song_key),
	UNIQUE (song_id, song_name)
);

CREATE TABLE IF NOT EXISTS d_app_user (
	user_key SERIAL,
	first_name TEXT,
	last_name TEXT,
	gender VARCHAR(1),
	level TEXT,
	PRIMARY KEY (user_key),
	UNIQUE (first_name, last_name)
);

CREATE TABLE IF NOT EXISTS d_timestamp (
	timestamp_key SERIAL,
	second INT NOT NULL,
	minute INT NOT NULL,
	hour INT NOT NULL,
	day INT NOT NULL,
	month INT NOT NULL,
	year INT NOT NULL,
	weekday BOOL NOT NULL,
	timestamp BIGINT NOT NULL,
	user_key INT REFERENCES d_app_user(user_key),
	PRIMARY KEY (timestamp_key)
);

CREATE TABLE IF NOT EXISTS f_songplay (
	songplay_key SERIAL,
	start_time BIGINT NOT NULl,
	user_key INT REFERENCES d_app_user(user_key),
	level TEXT NOT NULL,
	song_key INT REFERENCES d_song(song_key),
	artist_key INT REFERENCES d_artist(artist_key),
	session_id INT NOT NULL,
	PRIMARY KEY (songplay_key)
);