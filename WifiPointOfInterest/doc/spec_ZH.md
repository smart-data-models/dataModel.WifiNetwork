<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体WifiPointOfInterest  
=====================<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.WifiNetwork/blob/master/WifiPointOfInterest/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全局描述：**该实体描述了拥有无线网络的兴趣点**  
版本： 0.1.0  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 属性列表  

<sup><sub>[*] 如果属性中没有类型，是因为它可能有多个类型或不同的格式/模式</sub></sup>。  
- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 国家。例如，西班牙  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 街道地址所在的地点，以及该地点所在的区域  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: 地点所在的地区，以及该地区位于哪个国家  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 地区是一种行政区划，在一些国家由地方政府管理    
	- `postOfficeBoxNumber[string]`: 用于邮政信箱地址的邮政信箱号码。例如：03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 邮政编码。例如：24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 街道地址  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
- `alternateName[string]`: 该项目的替代名称  - `areaServed[string]`: 提供服务或提供物品的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `category[array]`: 该兴趣点的类别。允许值：由[事实分类](https://github.com/Factual/places/blob/master/categories/factual_taxonomy.json)定义的类别，以及数据模型用户可能实现的其他类别  . Model: [https://schema.org/Number](https://schema.org/Number)- `clientsConnected[number]`: 该兴趣点连接的客户或用户数量  . Model: [https://schema.org/Number](https://schema.org/Number)- `dataProvider[string]`: 标识统一数据实体提供者的字符序列  - `dateCreated[date-time]`: 实体创建时间戳。通常由存储平台分配  - `dateModified[date-time]`: 实体最后一次修改的时间戳。通常由存储平台分配  - `description[string]`: 项目描述  - `email[idn-email]`: 所有者的电子邮件地址  - `id[*]`: 实体的唯一标识符  - `location[*]`: 项目的 Geojson 引用。它可以是点、线条字符串、多边形、多点、多线条字符串或多多边形  - `name[string]`: 该项目的名称  - `owner[array]`: 包含一个 JSON 编码字符序列的列表，其中引用了所有者的唯一 Ids  - `seeAlso[*]`: 指向有关该项目的其他资源的 uri 列表  - `service[array]`: 该属性用于将接入点分配给接受无线服务的一个或多个市政服务部门。例如图书馆、博物馆、社会服务、体育  . Model: [https://schema.org/Number](https://schema.org/Number)- `source[string]`: 以 URL 形式给出实体数据原始来源的字符串。建议使用源提供者的完全合格域名或源对象的 URL  - `timeInstant[date-time]`: 有效载荷的时间戳。在生产环境中，属性类型可能等同于 `ISO8601`字符串。如果是这样，则必须将其视为 `DateTime` 的同义词。保留该属性是为了向后兼容旧的 FIWARE 参考实现。  . Model: [https://schema.org/Datetime](https://schema.org/Datetime)- `type[string]`: 必须是 WifiPointOfInterest。  - `wifiStatus[string]`: 表示该地点是否有无线网络及其提供的服务。允许的值有noService "表示兴趣点没有安装接入点；"working "表示兴趣点安装了接入点，且所有接入点都能正常工作（正常）；"totalFailure "表示兴趣点安装了接入点，但所有接入点都不能正常工作（故障）；"workingPartially "表示兴趣点安装了接入点，其中一些能正常工作（正常），另一些不能正常工作（故障）。枚举："无服务、全部故障、工作、部分工作  . Model: [https://schema.org/Text](https://schema.org/Text)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
所需属性  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
该数据模型是与[巴伦西亚市政厅](https://www.valencia.es)合作开发的。  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 属性的数据模型描述  
按字母顺序排列（点击查看详情）  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
WifiPointOfInterest:    
  description: This entity describes a Point of Interest that has a wireless network    
  properties:    
    address:    
      description: The mailing address    
      properties:    
        addressCountry:    
          description: 'The country. For example, Spain'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressCountry    
            type: Property    
        addressLocality:    
          description: 'The locality in which the street address is, and which is in the region'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressLocality    
            type: Property    
        addressRegion:    
          description: 'The region in which the locality is, and which is in the country'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressRegion    
            type: Property    
        district:    
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government'    
          type: string    
          x-ngsi:    
            type: Property    
        postOfficeBoxNumber:    
          description: 'The post office box number for PO box addresses. For example, 03578'    
          type: string    
          x-ngsi:    
            model: https://schema.org/postOfficeBoxNumber    
            type: Property    
        postalCode:    
          description: 'The postal code. For example, 24004'    
          type: string    
          x-ngsi:    
            model: https://schema.org/https://schema.org/postalCode    
            type: Property    
        streetAddress:    
          description: The street address    
          type: string    
          x-ngsi:    
            model: https://schema.org/streetAddress    
            type: Property    
        streetNr:    
          description: Number identifying a specific property on a public street    
          type: string    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: An alternative name for this item    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: The geographic area where a service or offered item is provided    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    category:    
      description: 'Category of this point of interest. Allowed values: Those defined by the [Factual taxonomy](https://github.com/Factual/places/blob/master/categories/factual_taxonomy.json) together with other categories that the user of the data model may implement'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    clientsConnected:    
      description: Number of clients or users connected in this point of interest    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    dataProvider:    
      description: A sequence of characters identifying the provider of the harmonised data entity    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: Entity creation timestamp. This will usually be allocated by the storage platform    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    email:    
      description: Email address of owner    
      format: idn-email    
      type: string    
      x-ngsi:    
        type: Property    
    id:    
      anyOf:    
        - description: Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
          x-ngsi:    
            type: Property    
        - description: Identifier format of any NGSI entity    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
      description: Unique identifier of the entity    
      x-ngsi:    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: Geojson reference to the item. Point    
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
          title: GeoJSON Point    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. LineString    
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
          title: GeoJSON LineString    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. Polygon    
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
          title: GeoJSON Polygon    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiPoint    
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
          title: GeoJSON MultiPoint    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiLineString    
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
          title: GeoJSON MultiLineString    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiLineString    
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
          title: GeoJSON MultiPolygon    
          type: object    
          x-ngsi:    
            type: GeoProperty    
      x-ngsi:    
        type: GeoProperty    
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf:    
          - description: Identifier format of any NGSI entity    
            maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
            x-ngsi:    
              type: Property    
          - description: Identifier format of any NGSI entity    
            format: uri    
            type: string    
            x-ngsi:    
              type: Property    
        description: Unique identifier of the entity    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        type: Property    
    seeAlso:    
      description: list of uri pointing to additional resources about the item    
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
      description: 'This attribute is used to assign the access point to one or several municipal service departments that receive the wireless service. For example: Library, Museums, Social Services, Sports'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
      type: string    
      x-ngsi:    
        type: Property    
    timeInstant:    
      description: 'Timestamp of the payload . There can be production environments where the attribute type is equal to the `ISO8601` string. If so, it must be considered as a synonym of `DateTime`. This attribute is kept for backwards compatibility with old FIWARE reference implementations'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Datetime    
        type: Property    
    type:    
      description: NGSI Entity type. it has to be WifiPointOfInterest    
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
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.WifiNetwork/blob/master/WifiPointOfInterest/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.WifiNetwork/WifiPointOfInterest/schema.json    
  x-model-tags: ""    
  x-version: 0.1.0    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## 有效载荷示例  
#### WifiPointOfInterest NGSI-v2 键值示例  
下面是一个以 JSON-LD 格式作为键值的 WifiPointOfInterest 示例。当使用 `options=keyValues` 时，这与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### WifiPointOfInterest NGSI-v2 标准化示例  
下面是一个 WifiPointOfInterest 的示例，格式为规范化的 JSON-LD。在不使用选项的情况下，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### WifiPointOfInterest NGSI-LD 键值示例  
下面是一个以 JSON-LD 格式作为键值的 WifiPointOfInterest 示例。当使用 `options=keyValues` 时，这与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "poi_226",  
    "type": "WifiPointOfInterest",  
    "address": {  
        "streetAddress": "Avda. Plata, 26. ",  
        "addressLocality": "Valencia"  
    },  
    "category": [  
        "70-Servicios de Emergencia"  
    ],  
    "clientsConnected": 1563,  
    "dataProvider": "B\u00fasqueda del nombre/direcci\u00f3n en google",  
    "description": "Edificio del Parque Central de Bomberos",  
    "email": "asistencia_tecnica_wifi@valencia.es",  
    "location": {  
        "type": "Point",  
        "coordinates": [  
            -0.367589,  
            39.454197  
        ]  
    },  
    "name": "Parque Central de Bomberos",  
    "service": [  
        "Bomberos"  
    ],  
    "source": "",  
    "timeInstant": "2020-09-22T09:30:03.00Z",  
    "wifiStatus": "working",  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.WifiNetwork/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### WifiPointOfInterest NGSI-LD 归一化示例  
下面是一个 WifiPointOfInterest 的示例，格式为规范化的 JSON-LD。在不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "poi_226",  
    "type": "WifiPointOfInterest",  
    "TimeInstant": {  
        "type": "DateTime",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2020-09-22T09:30:03.00Z"  
        }  
    },  
    "address": {  
        "type": "Property",  
        "value": "Avda. Plata, 26. Valencia"  
    },  
    "category": {  
        "type": "Property",  
        "value": [  
            "70-Servicios de Emergencia"  
        ]  
    },  
    "clientsConnected": {  
        "type": "Property",  
        "value": 1563  
    },  
    "contactPoint": {  
        "type": "Property",  
        "value": "asistencia_tecnica_wifi@valencia.es"  
    },  
    "dataProvider": {  
        "type": "Property",  
        "value": "B\u00fasqueda del nombre/direcci\u00f3n en google"  
    },  
    "description": {  
        "type": "Property",  
        "value": "Edificio del Parque Central de Bomberos"  
    },  
    "location": {  
        "type": "GeoProperty",  
        "value": {  
            "type": "Point",  
            "coordinates": [  
                -0.367589,  
                39.454197  
            ]  
        }  
    },  
    "name": {  
        "type": "Property",  
        "value": "Parque Central de Bomberos"  
    },  
    "service": {  
        "type": "Property",  
        "value": [  
            "Bomberos"  
        ]  
    },  
    "source": {  
        "type": "Property",  
        "value": ""  
    },  
    "wifiStatus": {  
        "type": "Property",  
        "value": "working"  
    }  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
请参阅 [FAQ 10](https://smartdatamodels.org/index.php/faqs/)，获取如何处理幅度单位的答案。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
