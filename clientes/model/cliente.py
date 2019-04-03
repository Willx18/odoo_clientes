# -*- coding: utf-8 -*-
from odoo import api, exceptions, fields, models, _

class cliente(models.Model):

    _name = 'clientes.cliente'


    name = fields.Char(string='Nombre', required=True)

    identidad = fields.Char(string='Identidad')

    rtn= fields.Char(string='RTN')
    
    genero = fields.Selection(string='Género', 
        selection=[('m', 'Másculino'), ('f', 'Feménino'),])

    correo_e= direccion=fields.Char(string='Correo electronico')

    fecha_nacimiento = fields.Date(string='Fecha de Nacimiento')

    direccion=fields.Char(string='Direccion')

    telefono=fields.Char(string='Numero telefonico')

    
    


    

    
 
    
    