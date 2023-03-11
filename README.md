# monitoring url with python+plotly+mysql (monitorando url com python+plotly+mysql)
Monitoramento de url com python 3.8 usando plotly com acesso a banco mysql para consulta das urls inseridas em tabela1
![monitor_url](https://user-images.githubusercontent.com/70037523/182167871-25368d5e-56df-4df5-a749-664d14aa3791.png)


# Table structure (Estrutura da tabela no banco mysql)
-- banco.tabela1 definition

CREATE TABLE `tabela1` (
  `id` int NOT NULL AUTO_INCREMENT,
  `url` text,
  `app` text,
  `local` text,
  `cod_error` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb3;

# Data Insert (Insert de dados)
INSERT INTO banco.tabela1
(id, url, app, `local`)
VALUES(1, 'http://192.168.1.20/dokuwiki/', 'DOKUWIKI', 'Rack1 - Servidor HP', );
INSERT INTO banco.tabela1
(id, url, app, `local`)
VALUES(2, 'http://192.168.1.21', 'APACHE2', 'Rack2 - Torre Dell');
INSERT INTO banco.tabela1
(id, url, app, `local`)
VALUES(3, 'http://192.168.1.23/phpipam', 'PHPIPAM', 'Rack1 - Servidor HP');
INSERT INTO banco.tabela1
(id, url, app, `local`)
VALUES(4, 'http://redmine.dominio.com.br/', 'REDMINE', 'Kubernetes Container - VMware Server');
INSERT INTO banco.tabela1
(id, url, app, `local`)
VALUES(5, 'http://192.168.1.25', 'NGINX', 'Rack1 - Servidor HP ');

# How do execute (Como executar):
Access the directory and run docker command (Acesse o diretório e execute o comando docker).
- cd monitoring-url-python
- docker build -t monitolocalhost/monitoramento-pyramento-py:v1.0 .
- docker run -p 8050:8050 --name monitor-py -d localhost/monitoramento-py:v1.0 
