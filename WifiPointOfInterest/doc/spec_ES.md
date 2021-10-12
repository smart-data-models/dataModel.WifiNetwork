Entidad: WifiPointOfInterest  
============================  
[Licencia abierta](https://github.com/smart-data-models//dataModel.WifiNetwork/blob/master/WifiPointOfInterest/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descripción global: **Esta entidad describe un punto de interés que tiene una red inalámbrica**  
versión: 0.1.0  

## Lista de propiedades  

- `address`: La dirección postal  - `alternateName`: Un nombre alternativo para este artículo  - `areaServed`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  - `category`: Categoría de este punto de interés. Valores permitidos: Los definidos por la [Taxonomía factual](https://github.com/Factual/places/blob/master/categories/factual_taxonomy.json) junto con otras categorías que el usuario del modelo de datos pueda implementar.  - `clientsConnected`: Número de clientes o usuarios conectados en este punto de interés.  - `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated`: Marca de tiempo de creación de la entidad. Suele ser asignada por la plataforma de almacenamiento.  - `dateModified`: Marca de tiempo de la última modificación de la entidad. Normalmente será asignada por la plataforma de almacenamiento.  - `description`: Una descripción de este artículo  - `email`: Dirección de correo electrónico del propietario.  - `id`: Identificador único de la entidad  - `location`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `name`: El nombre de este artículo.  - `owner`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios  - `seeAlso`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `service`: Este atributo se utiliza para asignar el punto de acceso a uno o varios departamentos de servicios municipales que reciben el servicio inalámbrico. Por ejemplo: Biblioteca, Museos, Servicios Sociales, Deportes...  - `source`: Una secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `timeInstant`: Marca de tiempo de la carga útil . Puede haber entornos de producción en los que el tipo de atributo sea igual a la cadena `ISO8601`. Si es así, debe considerarse como un sinónimo de `DateTime`. Este atributo se mantiene por compatibilidad con las antiguas implementaciones de referencia de FIWARE.  - `type`: Tipo de entidad NGSI. Tiene que ser WifiPointOfInterest  - `wifiStatus`: Indica si hay una red inalámbrica disponible en esta ubicación y el servicio que presta. Los valores permitidos son: 'noService' cuando el punto de interés no tiene puntos de acceso instalados, 'working' cuando el punto de interés tiene puntos de acceso instalados y todos ellos están funcionando (up), 'totalFailure' cuando el punto de interés tiene puntos de acceso instalados y todos ellos no están funcionando (down), y 'workingPartially' cuando el punto de interés tiene puntos de acceso instalados y algunos de ellos están funcionando (up) y otros no (down). Enum:'noService, totalFailure, working, workingPartially'    
Propiedades requeridas  
- `id`  - `type`    
Este modelo de datos se ha desarrollado en colaboración con el [Ayuntamiento de Valencia](https://www.valencia.es).  
## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
WifiPointOfInterest:    
  description: 'This entity describes a Point of Interest that has a wireless network'    
  properties:    
    address:    
      description: 'The mailing address'    
      properties:    
        addressCountry:    
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/addressCountry'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/addressLocality'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/addressRegion'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, 03578. Model:''https://schema.org/postOfficeBoxNumber'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, 24004. Model:''https://schema.org/https://schema.org/postalCode'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/streetAddress'''    
          type: string    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    category:    
      description: 'Category of this point of interest. Allowed values: Those defined by the [Factual taxonomy](https://github.com/Factual/places/blob/master/categories/factual_taxonomy.json) together with other categories that the user of the data model may implement.'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    clientsConnected:    
      description: 'Number of clients or users connected in this point of interest.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    email:    
      description: 'Email address of owner.'    
      format: idn-email    
      type: string    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: &wifipointofinterest_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Unique identifier of the entity'    
      x-ngsi:    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: 'Geoproperty. Geojson reference to the item. Point'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                type: number    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - Point    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON Point'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. LineString'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - LineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON LineString'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. Polygon'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 4    
                type: array    
              type: array    
            type:    
              enum:    
                - Polygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON Polygon'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiPoint'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPoint    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiPoint'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiLineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiLineString'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    items:    
                      type: number    
                    minItems: 2    
                    type: array    
                  minItems: 4    
                  type: array    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPolygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiPolygon'    
          type: object    
      x-ngsi:    
        type: Geoproperty    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *wifipointofinterest_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    seeAlso:    
      description: 'list of uri pointing to additional resources about the item'    
      oneOf:    
        - items:    
            format: uri    
            type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      x-ngsi:    
        type: Property    
    service:    
      description: 'This attribute is used to assign the access point to one or several municipal service departments that receive the wireless service. For example: Library, Museums, Social Services, Sports...'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    timeInstant:    
      description: 'Timestamp of the payload . There can be production environments where the attribute type is equal to the `ISO8601` string. If so, it must be considered as a synonym of `DateTime`. This attribute is kept for backwards compatibility with old FIWARE reference implementations.'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Datetime    
        type: Property    
    type:    
      description: 'NGSI Entity type. it has to be WifiPointOfInterest'    
      enum:    
        - WifiPointOfInterest    
      type: string    
      x-ngsi:    
        type: Property    
    wifiStatus:    
      description: 'Indicates if there is a wireless network available at    this location and the service that it is providing. The allowed values are: ''noService'' when the point of interest has no access points installed, ''working'' when the point of interest has access points installed and all of them are working (up), ''totalFailure'' when the point of interest has access points installed and all of them are not working (down), and ''workingPartially'' when the point of interest has access points installed and some of them are working (up) and some of then are not working (down). Enum:''noService, totalFailure, working, workingPartially'''    
      enum:    
        - noService    
        - totalFailure    
        - working    
        - workingPartially    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  version: 0.1.0    
```  
</details>    
## Ejemplo de carga útil  
#### WifiPointOfInterest NGSI-v2 key-values Ejemplo  
Aquí hay un ejemplo de un WifiPointOfInterest en formato JSON-LD como valores-clave. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "poi_226",  
  "type": "WifiPointOfInterest",  
  "name": "Parque Central de Bomberos",  
  "address": {  
    "streetAddress": "Avda. Plata, 26. ",  
    "addressLocality": "Valencia"  
  },  
  "location": {  
    "type": "Point",  
    "coordinates": [-0.367589, 39.454197]  
  },  
  "clientsConnected": 1563,  
  "wifiStatus": "working",  
  "service": ["Bomberos"],  
  "category": ["70-Servicios de Emergencia"],  
  "timeInstant": "2020-09-22T09:30:03.00Z",  
  "email": "asistencia_tecnica_wifi@valencia.es",  
  "dataProvider": "Búsqueda del nombre/dirección en google",  
  "description": "Edificio del Parque Central de Bomberos",  
  "source": ""  
}  
```  
#### WifiPointOfInterest NGSI-v2 normalizado Ejemplo  
Este es un ejemplo de un WifiPointOfInterest en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "poi_226",  
  "type": "WifiPointOfInterest",  
  "name": {  
    "type": "Text",  
    "value": "Parque Central de Bomberos"  
  },  
  "address": {  
    "type": "Text",  
    "value": "Avda. Plata, 26. Valencia"  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -0.367589,  
        39.454197  
      ]  
    }  
  },  
  "clientsConnected": {  
    "type": "Number",  
    "value": 1563  
  },  
  "wifiStatus": {  
    "type": "Text",  
    "value": "working"  
  },  
  "service": {  
    "type": "Array",  
    "value": [  
      "Bomberos"  
    ]  
  },  
  "category": {  
    "type": "Array",  
    "value": [  
      "70-Servicios de Emergencia"  
    ]  
  },  
  "TimeInstant": {  
    "type": "DateTime",  
    "value": "2020-09-22T09:30:03.00Z"  
  },  
  "contactPoint": {  
    "type": "Text",  
    "value": "asistencia_tecnica_wifi@valencia.es"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "Búsqueda del nombre/dirección en google"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Edificio del Parque Central de Bomberos"  
  },  
  "source": {  
    "type": "Text",  
    "value": ""  
  }  
}  
```  
#### WifiPointOfInterest NGSI-LD key-values Ejemplo  
Aquí hay un ejemplo de un WifiPointOfInterest en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "poi_226",  
  "type": "WifiPointOfInterest",  
  "name": "Parque Central de Bomberos",  
  "address": {  
    "streetAddress": "Avda. Plata, 26. ",  
    "addressLocality": "Valencia"  
  },  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -0.367589,  
      39.454197  
    ]  
  },  
  "clientsConnected": 1563,  
  "wifiStatus": "working",  
  "service": [  
    "Bomberos"  
  ],  
  "category": [  
    "70-Servicios de Emergencia"  
  ],  
  "timeInstant": "2020-09-22T09:30:03.00Z",  
  "email": "asistencia_tecnica_wifi@valencia.es",  
  "dataProvider": "Búsqueda del nombre/dirección en google",  
  "description": "Edificio del Parque Central de Bomberos",  
  "source": "",  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
#### WifiPointOfInterest NGSI-LD normalizado Ejemplo  
Este es un ejemplo de un WifiPointOfInterest en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "poi_226",  
  "type": "WifiPointOfInterest",  
  "name": {  
    "type": "Property",  
    "value": "Parque Central de Bomberos"  
  },  
  "address": {  
    "type": "Property",  
    "value": "Avda. Plata, 26. Valencia"  
  },  
  "location": {  
    "type": "Geoproperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -0.367589,  
        39.454197  
      ]  
    }  
  },  
  "clientsConnected": {  
    "type": "Property",  
    "value": 1563  
  },  
  "wifiStatus": {  
    "type": "Property",  
    "value": "working"  
  },  
  "service": {  
    "type": "Property",  
    "value": [  
      "Bomberos"  
    ]  
  },  
  "category": {  
    "type": "Property",  
    "value": [  
      "70-Servicios de Emergencia"  
    ]  
  },  
  "TimeInstant": {  
    "type": "DateTime",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2020-09-22T09:30:03.00Z"  
    }  
  },  
  "contactPoint": {  
    "type": "Property",  
    "value": "asistencia_tecnica_wifi@valencia.es"  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "Búsqueda del nombre/dirección en google"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Edificio del Parque Central de Bomberos"  
  },  
  "source": {  
    "type": "Property",  
    "value": ""  
  }  
}  
```  
