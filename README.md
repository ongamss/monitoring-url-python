# monitoring url with python+plotly+mysql (monitorando url com python+plotly+mysql)
Monitoramento de url com python 3.8 usando plotly com acesso a banco mysql para cadastro das urls


# Table structure (Estrutura da tabela no banco mysql)
-- banco.tabela1 definition

CREATE TABLE `tabela1` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url` text,
  `app` text,
  `local` text,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=22 DEFAULT CHARSET=utf8;

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
