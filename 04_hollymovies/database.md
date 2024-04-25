# Database

## Tables

###  users

- id
- username
- password
- name ?
- surname ?
- email
- telephone ?
- avatar

###  peoples

- id
- name
- surname
- date_of_birth
- date_of_death
- place_of_birth
- place_of_death
- country
- biography
- status
- photos
- awards -> n:m

###  movies

- id
- title_orig
- title_cz
- release_year
- date_of_premiere
- genres -> m:n 
- countries -> m:n
- length (min)
- languages -> m:n ?
- directors -> m:n
- actors -> m:n
- multimedia -> multimedia 1:n
- awards -> n:m
- companies -> n:m companies

### series

- id
- pilot ?
- episodes -> 1:n

### multimedia

- id
- url
- type (video, picture, main_picture)
- movie -> FK movies
- actors -> n:m
- text
- alt_text

###  genres

- id
- name

###  reviews

- id
- text
- rating
- user -> FK users
- movie -> FK movies
- time 

###  awards

- id
- date
- name

###  companies

- id
- name
