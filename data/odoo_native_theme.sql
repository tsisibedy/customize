DELETE from customize_base where name = 'Odoo native';
INSERT INTO customize_base (name, o_skew_gradient_primary,o_skew_gradient_second, odoo_brand_primary,brand_optional)
VALUES ('Odoo native','#77717e', '#c9a8a9', '#875A7B', '#21b799');
DELETE from customize_base where name = 'Cenoel theme';
INSERT INTO customize_base (name, o_skew_gradient_primary,o_skew_gradient_second, odoo_brand_primary,brand_optional)
VALUES ('Cenoel theme','#003321', '#00472E', '#003321', '#002417');