---
layout: default
---


# Latest Data Breaches

{% for post in site.categories.breaches %}
  💀 {{ post.date | date_to_string }} ~ <b>{{ post.title }}</b> ~[download preview]({{ post.download }}) [buy full for 10 BTC or 200 ETH]({{ post.url }}) 
{% endfor %}
---
