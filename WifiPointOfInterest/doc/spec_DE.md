Entität: WifiPointOfInterest  
============================







- `id`  



<details><summary><strong>full yaml details</strong></summary>    

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
        areaServed:    
          description: 'Property. The geographic area where a service or offered item is provided. Model:''https://schema.org/areaServed'''    
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
      type: Property    
      x-ngsi:    
        model: https://schema.org/address    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    category:    
      description: 'Category of this point of interest. Allowed values: Those defined by the [Factual taxonomy](https://github.com/Factual/places/blob/master/categories/factual_taxonomy.json) together with other categories that the user of the data model may implement.'    
      items:    
        type: string    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    clientsConnected:    
      description: 'Number of clients or users connected in this point of interest.'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    description:    
      description: 'A description of this item'    
      type: Property    
    email:    
      description: 'Email address of owner.'    
      format: idn-email    
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
      type: Property    
    location:    
      $id: https://geojson.org/schema/Geometry.json    
      $schema: "http://json-schema.org/draft-07/schema#"    
      oneOf:    
        - properties:    
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
        - properties:    
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
        - properties:    
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
        - properties:    
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
        - properties:    
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
        - properties:    
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
      title: 'GeoJSON Geometry'    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *wifipointofinterest_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
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
      type: Property    
    service:    
      description: 'This attribute is used to assign the access point to one or several municipal service departments that receive the wireless service. For example: Library, Museums, Social Services, Sports...'    
      items:    
        type: string    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    timeInstant:    
      description: "[Timestamp](https://github.com/telefonicaid/iotagent-node-lib#TimeInstant) saved by FIWARE's IoT Agent. Note: This attribute has not been harmonized to keep backwards compatibility with current FIWARE reference implementations. There can be production environments where the attribute type is equal to the 'ISO8601' string. If so, it must be considered as a synonym of 'DateTime'."    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: https://schema.org/DateTime    
    type:    
      description: 'NGSI Entity type. it has to be WifiPointOfInterest'    
      enum:    
        - WifiPointOfInterest    
      type: Property    
    wifiStatus:    
      description: 'Indicates if there is a wireless network available at    this location and the service that it is providing. The allowed values are: ''noService'' when the point of interest has no access points installed, ''working'' when the point of interest has access points installed and all of them are working (up), ''totalFailure'' when the point of interest has access points installed and all of them are not working (down), and ''workingPartially'' when the point of interest has access points installed and some of them are working (up) and some of then are not working (down). Enum:''noService, totalFailure, working, workingPartially'''    
      enum:    
        - noService    
        - totalFailure    
        - working    
        - workingPartially    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
  required:    
    - id    
    - type    
  type: object    
```  
</details>    





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