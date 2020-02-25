# WordPress Good Defaults

**WordPress Good Defaults** is an example project of a WordPress application that uses a MySQL database and a phpMyAdmin server to administrate the database.

## Contents

- [Dependencies](#dependencies)
- [Configuration](#configuration)
- [Run](#run)
- [Authors](#Authors)

---

## Dependencies

![WordPress](https://img.shields.io/badge/wordpress-+5-black.svg)
![Docker](https://img.shields.io/badge/docker-+19-blue.svg)
![phpMyAdmin](https://img.shields.io/badge/phpMyAdmin-+5-orange.svg)

---

## Configuration

### Database

To run this system it's necessary an **environment file** (**.env**) in the *db* folder, `./wpdb/db.env`.

``` bash
touch db.env
```

``` bash
vi db.env
```

Then, here's a list of the variables needed with its default value.

#### MySQL Environment Variables

| Variable             | Value                  |
|----------------------|------------------------|
| MYSQL_ROOT_PASSWORD  | rootpass               |
| MYSQL_USER           | wpuser                 |
| MYSQL_PASSWORD       | wppass                 |
| MYSQL_DATABASE       | wpdb                   |

### phpMyAdmin

To run this system it's necessary an **environment file** (**.env**) in the *pma* folder, `./pma/pma.env`.

``` bash
touch pma.env
```

``` bash
vi pma.env
```

Then, here's a list of the variables needed with its default value.

#### phpMyAdmin Environment Variables

| Variable             | Value                  |
|----------------------|------------------------|
| PMA_HOST             | wpdb-dns:3306          |
| MYSQL_ROOT_PASSWORD  | rootpass               |

### WordPress

To run this system it's necessary an **environment file** (**.env**) in the *wp* folder, `./wp/wp.env`.

``` bash
touch wp.env
```

``` bash
vi wp.env
```

Then, here's a list of the variables needed with its default value.

#### WordPress Environment Variables

| Variable                 | Value                  |
|--------------------------|------------------------|
| WORDPRESS_DB_HOST        | wpdb-dns:3306          |
| WORDPRESS_DB_USER        | wpuser                 |
| WORDPRESS_DB_PASSWORD    | wppass                 |
| WORDPRESS_DB_NAME        | wpdb                   |

## Authors

***David Martinez** - [Davestring](https://github.com/Davestring)