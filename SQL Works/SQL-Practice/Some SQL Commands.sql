use moviesdb;
select count(*) from actors where birth_year = 1986;
select * from movies where title like '%Captain%';
select * from movies where studio like '';
select distinct birth_year from actors;
select * from movies where imdb_rating>=7 and imdb_rating<=9;
select * from movies where imdb_rating between 7 and 9;
select * from movies where release_year = 2022 or release_year = 2019;
select * from movies where release_year in (2022,2019);
select * from movies where imdb_rating is null;
select * from movies order by imdb_rating asc;
select * from movies order by imdb_rating desc limit 5 offset 2;
select min(imdb_rating) from movies;
select round(avg(imdb_rating),2) from movies where title like '%thor%';
select max(imdb_rating) as max_rating, count(*) as cnt from movies where studio!='' group by studio order by cnt desc;
select max(imdb_rating) as max_rating, count(*) as cnt from movies group by studio having cnt>2 order by cnt desc;
select * , year(curdate())-birth_year as age from actors;
select * , case when currency = 'INR' then (revenue-budget)/83.1 when unit = 'Billions' then (revenue-budget)*1000 when unit = 'Thousands' then (revenue-budget)/1000 else (revenue-budget) end as net_std_profit from financials;
select * from movies
full join financials on movies.movie_id=financials.movie_id;


