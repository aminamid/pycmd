## Mon Feb  9 21:57:59 JST 2015

### only slugs

```
"nyc1"
"ams1"
"sfo1"
"nyc2"
"ams2"
"sgp1"
"lon1"
"nyc3"
"ams3"
```

```
"512mb"
"1gb"
"2gb"
"4gb"
"8gb"
"16gb"
```

```
null
null
null
"coreos-alpha"
"coreos-beta"
"coreos-stable"
"fedora-20-x64"
"fedora-20-x32"
"fedora-19-x64"
"fedora-19-x32"
"centos-5-8-x64"
"centos-5-8-x32"
"debian-6-0-x64"
"debian-6-0-x32"
"fedora-21-x64"
"ubuntu-14-04-x32"
"ubuntu-14-04-x64"
"ubuntu-14-10-x32"
"ubuntu-14-10-x64"
"freebsd-10-1-x64"
```

### regions

```json
[
  {
    "slug": "nyc1",
    "name": "New York 1",
    "features": [
      "virtio",
      "backups"
    ],
    "sizes": [],
    "available": false
  },
  {
    "slug": "ams1",
    "name": "Amsterdam 1",
    "features": [
      "virtio",
      "backups"
    ],
    "sizes": [],
    "available": false
  },
  {
    "slug": "sfo1",
    "name": "San Francisco 1",
    "features": [
      "virtio",
      "backups",
      "ipv6",
      "metadata"
    ],
    "sizes": [
      "32gb",
      "16gb",
      "2gb",
      "1gb",
      "4gb",
      "8gb",
      "512mb",
      "64gb",
      "48gb"
    ],
    "available": true
  },
  {
    "slug": "nyc2",
    "name": "New York 2",
    "features": [
      "virtio",
      "private_networking",
      "backups"
    ],
    "sizes": [
      "32gb",
      "16gb",
      "2gb",
      "1gb",
      "4gb",
      "8gb",
      "512mb",
      "64gb",
      "48gb"
    ],
    "available": true
  },
  {
    "slug": "ams2",
    "name": "Amsterdam 2",
    "features": [
      "virtio",
      "private_networking",
      "backups",
      "ipv6",
      "metadata"
    ],
    "sizes": [
      "32gb",
      "16gb",
      "2gb",
      "1gb",
      "4gb",
      "8gb",
      "512mb",
      "64gb",
      "48gb"
    ],
    "available": true
  },
  {
    "slug": "sgp1",
    "name": "Singapore 1",
    "features": [
      "virtio",
      "private_networking",
      "backups",
      "ipv6",
      "metadata"
    ],
    "sizes": [
      "32gb",
      "16gb",
      "2gb",
      "1gb",
      "4gb",
      "8gb",
      "512mb",
      "64gb",
      "48gb"
    ],
    "available": true
  },
  {
    "slug": "lon1",
    "name": "London 1",
    "features": [
      "virtio",
      "private_networking",
      "backups",
      "ipv6",
      "metadata"
    ],
    "sizes": [
      "32gb",
      "16gb",
      "2gb",
      "1gb",
      "4gb",
      "8gb",
      "512mb",
      "64gb",
      "48gb"
    ],
    "available": true
  },
  {
    "slug": "nyc3",
    "name": "New York 3",
    "features": [
      "virtio",
      "private_networking",
      "backups",
      "ipv6",
      "metadata"
    ],
    "sizes": [
      "32gb",
      "16gb",
      "2gb",
      "1gb",
      "4gb",
      "8gb",
      "512mb",
      "64gb",
      "48gb"
    ],
    "available": true
  },
  {
    "slug": "ams3",
    "name": "Amsterdam 3",
    "features": [
      "virtio",
      "private_networking",
      "backups",
      "ipv6",
      "metadata"
    ],
    "sizes": [
      "32gb",
      "16gb",
      "2gb",
      "1gb",
      "4gb",
      "8gb",
      "512mb",
      "64gb",
      "48gb"
    ],
    "available": true
  }
]
```

### sizes

```json
[
  {
    "slug": "512mb",
    "disk": 20,
    "memory": 512,
    "vcpus": 1,
    "regions": [
      "nyc1",
      "sgp1",
      "ams1",
      "ams2",
      "sfo1",
      "nyc2",
      "lon1",
      "nyc3",
      "ams3"
    ],
    "price_hourly": 0.00744,
    "transfer": 1,
    "price_monthly": 5
  },
  {
    "slug": "1gb",
    "disk": 30,
    "memory": 1024,
    "vcpus": 1,
    "regions": [
      "nyc2",
      "sgp1",
      "ams1",
      "sfo1",
      "lon1",
      "nyc3",
      "ams3",
      "ams2",
      "nyc1"
    ],
    "price_hourly": 0.01488,
    "transfer": 2,
    "price_monthly": 10
  },
  {
    "slug": "2gb",
    "disk": 40,
    "memory": 2048,
    "vcpus": 2,
    "regions": [
      "nyc2",
      "sfo1",
      "ams1",
      "sgp1",
      "ams2",
      "lon1",
      "nyc3",
      "ams3",
      "nyc1"
    ],
    "price_hourly": 0.02976,
    "transfer": 3,
    "price_monthly": 20
  },
  {
    "slug": "4gb",
    "disk": 60,
    "memory": 4096,
    "vcpus": 2,
    "regions": [
      "nyc2",
      "sfo1",
      "ams1",
      "sgp1",
      "ams2",
      "lon1",
      "nyc3",
      "ams3",
      "nyc1"
    ],
    "price_hourly": 0.05952,
    "transfer": 4,
    "price_monthly": 40
  },
  {
    "slug": "8gb",
    "disk": 80,
    "memory": 8192,
    "vcpus": 4,
    "regions": [
      "nyc2",
      "sfo1",
      "sgp1",
      "ams1",
      "ams2",
      "nyc1",
      "lon1",
      "nyc3",
      "ams3"
    ],
    "price_hourly": 0.11905,
    "transfer": 5,
    "price_monthly": 80
  },
  {
    "slug": "16gb",
    "disk": 160,
    "memory": 16384,
    "vcpus": 8,
    "regions": [
      "sgp1",
      "nyc1",
      "sfo1",
      "ams2",
      "nyc3",
      "lon1",
      "nyc2",
      "ams1",
      "ams3"
    ],
    "price_hourly": 0.2381,
    "transfer": 6,
    "price_monthly": 160
  }
]
```

### images

```json
[
  {
    "public": false,
    "distribution": "CentOS",
    "regions": [
      "sgp1",
      "sgp1"
    ],
    "id": 4536807,
    "created_at": "2014-06-25T08:31:24Z",
    "name": "init",
    "slug": null,
    "min_disk_size": 40
  },
  {
    "public": false,
    "distribution": "CentOS",
    "regions": [
      "sgp1",
      "sgp1"
    ],
    "id": 4536808,
    "created_at": "2014-06-25T08:31:32Z",
    "name": "init",
    "slug": null,
    "min_disk_size": 40
  },
  {
    "public": false,
    "distribution": "CentOS",
    "regions": [
      "sgp1",
      "sgp1"
    ],
    "id": 4536809,
    "created_at": "2014-06-25T08:31:42Z",
    "name": "init",
    "slug": null,
    "min_disk_size": 40
  },
  {
    "public": true,
    "distribution": "CoreOS",
    "regions": [
      "nyc1",
      "ams1",
      "sfo1",
      "nyc2",
      "ams2",
      "sgp1",
      "lon1",
      "nyc3",
      "ams3",
      "nyc3"
    ],
    "id": 10321753,
    "created_at": "2015-01-28T15:50:19Z",
    "name": "575.0.0 (alpha)",
    "slug": "coreos-alpha",
    "min_disk_size": 20
  },
  {
    "public": true,
    "distribution": "CoreOS",
    "regions": [
      "nyc1",
      "ams1",
      "sfo1",
      "nyc2",
      "ams2",
      "sgp1",
      "lon1",
      "nyc3",
      "ams3",
      "nyc3"
    ],
    "id": 10321772,
    "created_at": "2015-01-28T15:53:03Z",
    "name": "557.1.0 (beta)",
    "slug": "coreos-beta",
    "min_disk_size": 20
  },
  {
    "public": true,
    "distribution": "CoreOS",
    "regions": [
      "nyc1",
      "ams1",
      "sfo1",
      "nyc2",
      "ams2",
      "sgp1",
      "lon1",
      "nyc3",
      "ams3",
      "nyc3"
    ],
    "id": 10324279,
    "created_at": "2015-01-28T18:20:50Z",
    "name": "522.6.0 (stable)",
    "slug": "coreos-stable",
    "min_disk_size": 20
  },
  {
    "public": true,
    "distribution": "Fedora",
    "regions": [
      "nyc1",
      "ams1",
      "sfo1",
      "nyc2",
      "ams2",
      "sgp1",
      "lon1",
      "nyc3",
      "ams3",
      "nyc3"
    ],
    "id": 6370882,
    "created_at": "2014-09-26T15:29:01Z",
    "name": "20 x64",
    "slug": "fedora-20-x64",
    "min_disk_size": 20
  },
  {
    "public": true,
    "distribution": "Fedora",
    "regions": [
      "nyc1",
      "ams1",
      "sfo1",
      "nyc2",
      "ams2",
      "sgp1",
      "lon1",
      "nyc3",
      "ams3",
      "nyc3"
    ],
    "id": 6370885,
    "created_at": "2014-09-26T15:29:18Z",
    "name": "20 x32",
    "slug": "fedora-20-x32",
    "min_disk_size": 20
  },
  {
    "public": true,
    "distribution": "Fedora",
    "regions": [
      "nyc1",
      "ams1",
      "sfo1",
      "nyc2",
      "ams2",
      "sgp1",
      "lon1",
      "nyc3",
      "ams3",
      "nyc3"
    ],
    "id": 6370968,
    "created_at": "2014-09-26T15:33:05Z",
    "name": "19 x64",
    "slug": "fedora-19-x64",
    "min_disk_size": 20
  },
  {
    "public": true,
    "distribution": "Fedora",
    "regions": [
      "nyc1",
      "ams1",
      "sfo1",
      "nyc2",
      "ams2",
      "sgp1",
      "lon1",
      "nyc3",
      "ams3",
      "nyc3"
    ],
    "id": 6370969,
    "created_at": "2014-09-26T15:33:39Z",
    "name": "19 x32",
    "slug": "fedora-19-x32",
    "min_disk_size": 20
  },
  {
    "public": true,
    "distribution": "CentOS",
    "regions": [
      "nyc1",
      "ams1",
      "sfo1",
      "nyc2",
      "ams2",
      "sgp1",
      "lon1",
      "nyc3",
      "ams3",
      "nyc3"
    ],
    "id": 6372321,
    "created_at": "2014-09-26T16:40:18Z",
    "name": "5.10 x64",
    "slug": "centos-5-8-x64",
    "min_disk_size": 20
  },
  {
    "public": true,
    "distribution": "CentOS",
    "regions": [
      "nyc1",
      "ams1",
      "sfo1",
      "nyc2",
      "ams2",
      "sgp1",
      "lon1",
      "nyc3",
      "ams3",
      "nyc3"
    ],
    "id": 6372425,
    "created_at": "2014-09-26T16:45:29Z",
    "name": "5.10 x32",
    "slug": "centos-5-8-x32",
    "min_disk_size": 20
  },
  {
    "public": true,
    "distribution": "Debian",
    "regions": [
      "nyc1",
      "ams1",
      "sfo1",
      "nyc2",
      "ams2",
      "sgp1",
      "lon1",
      "nyc3",
      "ams3",
      "nyc3"
    ],
    "id": 6372581,
    "created_at": "2014-09-26T16:56:00Z",
    "name": "6.0 x64",
    "slug": "debian-6-0-x64",
    "min_disk_size": 20
  },
  {
    "public": true,
    "distribution": "Debian",
    "regions": [
      "nyc1",
      "ams1",
      "sfo1",
      "nyc2",
      "ams2",
      "sgp1",
      "lon1",
      "nyc3",
      "ams3",
      "nyc3"
    ],
    "id": 6372662,
    "created_at": "2014-09-26T17:00:21Z",
    "name": "6.0 x32",
    "slug": "debian-6-0-x32",
    "min_disk_size": 20
  },
  {
    "public": true,
    "distribution": "Fedora",
    "regions": [
      "nyc1",
      "ams1",
      "sfo1",
      "nyc2",
      "ams2",
      "sgp1",
      "lon1",
      "nyc3",
      "ams3",
      "nyc3"
    ],
    "id": 9640922,
    "created_at": "2015-01-02T19:06:09Z",
    "name": "21 x64",
    "slug": "fedora-21-x64",
    "min_disk_size": 20
  },
  {
    "public": true,
    "distribution": "Ubuntu",
    "regions": [
      "nyc1",
      "ams1",
      "sfo1",
      "nyc2",
      "ams2",
      "sgp1",
      "lon1",
      "nyc3",
      "ams3",
      "nyc3"
    ],
    "id": 9801948,
    "created_at": "2015-01-08T18:40:58Z",
    "name": "14.04 x32",
    "slug": "ubuntu-14-04-x32",
    "min_disk_size": 20
  },
  {
    "public": true,
    "distribution": "Ubuntu",
    "regions": [
      "nyc1",
      "ams1",
      "sfo1",
      "nyc2",
      "ams2",
      "sgp1",
      "lon1",
      "nyc3",
      "ams3",
      "nyc3"
    ],
    "id": 9801950,
    "created_at": "2015-01-08T18:41:13Z",
    "name": "14.04 x64",
    "slug": "ubuntu-14-04-x64",
    "min_disk_size": 20
  },
  {
    "public": true,
    "distribution": "Ubuntu",
    "regions": [
      "nyc1",
      "ams1",
      "sfo1",
      "nyc2",
      "ams2",
      "sgp1",
      "lon1",
      "nyc3",
      "ams3",
      "nyc3"
    ],
    "id": 9801951,
    "created_at": "2015-01-08T18:41:22Z",
    "name": "14.10 x32",
    "slug": "ubuntu-14-10-x32",
    "min_disk_size": 20
  },
  {
    "public": true,
    "distribution": "Ubuntu",
    "regions": [
      "nyc1",
      "ams1",
      "sfo1",
      "nyc2",
      "ams2",
      "sgp1",
      "lon1",
      "nyc3",
      "ams3",
      "nyc3"
    ],
    "id": 9801954,
    "created_at": "2015-01-08T18:41:29Z",
    "name": "14.10 x64",
    "slug": "ubuntu-14-10-x64",
    "min_disk_size": 20
  },
  {
    "public": true,
    "distribution": "FreeBSD",
    "regions": [
      "sfo1",
      "ams2",
      "sgp1",
      "lon1",
      "nyc3",
      "ams3",
      "nyc3"
    ],
    "id": 10144573,
    "created_at": "2015-01-20T20:04:34Z",
    "name": "10.1",
    "slug": "freebsd-10-1-x64",
    "min_disk_size": 20
  }
]
```
