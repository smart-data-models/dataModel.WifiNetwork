<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
엔티티: 와이파이 관심 지점  
===============<!-- /10-Header -->  
<!-- 15-License -->  
[오픈 라이선스](https://github.com/smart-data-models//dataModel.WifiNetwork/blob/master/WifiPointOfInterest/LICENSE.md)  
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
글로벌 설명: **이 엔티티는 무선 네트워크가 있는 관심 지점**을 설명합니다.  
버전: 0.1.0  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 속성 목록  

<sup><sub>[*] 속성에 유형이 없는 것은 여러 유형 또는 다른 형식/패턴을 가질 수 있기 때문입니다</sub></sup>.  
- `address[object]`: 우편 주소  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 국가. 예를 들어, 스페인  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 도로명 주소가 있는 지역 및 해당 지역에 속한 지역  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: 해당 지역이 위치한 지역과 해당 국가의 지역  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 지구는 일부 국가에서는 지방 정부에서 관리하는 행정 구역의 일종입니다.    
	- `postOfficeBoxNumber[string]`: 사서함 주소의 우체국 사서함 번호입니다. 예: 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 우편 번호입니다. 예: 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 거리 주소  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: 공공 도로의 특정 건물을 식별하는 번호    
- `alternateName[string]`: 이 항목의 대체 이름  - `areaServed[string]`: 서비스 또는 제공 품목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)- `category[array]`: 이 관심 지점의 카테고리입니다. 허용된 값: 데이터 모델 사용자가 구현할 수 있는 다른 카테고리와 함께 [사실 분류법](https://github.com/Factual/places/blob/master/categories/factual_taxonomy.json)에 정의된 값입니다.  . Model: [https://schema.org/Number](https://schema.org/Number)- `clientsConnected[number]`: 이 관심 지점에 연결된 클라이언트 또는 사용자 수  . Model: [https://schema.org/Number](https://schema.org/Number)- `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `description[string]`: 이 항목에 대한 설명  - `email[idn-email]`: 소유자의 이메일 주소  - `id[*]`: 엔티티의 고유 식별자  - `location[*]`: 항목에 대한 지오숀 참조입니다. 포인트, 라인 문자열, 다각형, 멀티포인트, 멀티라인 문자열 또는 멀티폴리곤일 수 있습니다.  - `name[string]`: 이 항목의 이름  - `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `service[array]`: 이 속성은 무선 서비스를 수신하는 하나 또는 여러 지자체 서비스 부서에 액세스 포인트를 할당하는 데 사용됩니다. 예 도서관, 박물관, 사회 서비스, 스포츠  . Model: [https://schema.org/Number](https://schema.org/Number)- `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 문자 시퀀스입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `timeInstant[date-time]`: 페이로드의 타임스탬프입니다. 프로덕션 환경에서는 속성 유형이 `ISO8601` 문자열과 같을 수 있습니다. 이 경우 `DateTime`의 동의어로 간주해야 합니다. 이 속성은 이전 FIWARE 참조 구현과의 하위 호환성을 위해 유지됩니다.  . Model: [https://schema.org/Datetime](https://schema.org/Datetime)- `type[string]`: NGSI 엔티티 유형. 와이파이 관심 지점이어야 합니다.  - `wifiStatus[string]`: 이 위치에서 사용할 수 있는 무선 네트워크가 있는지 여부와 해당 네트워크가 제공하는 서비스를 나타냅니다. 허용되는 값은 다음과 같습니다: 관심 지점에 액세스 포인트가 설치되어 있지 않으면 'noService', 관심 지점에 액세스 포인트가 설치되어 있고 모두 작동 중이면 'working', 관심 지점에 액세스 포인트가 설치되어 있고 모두 작동하지 않으면 'totalFailure', 관심 지점에 액세스 포인트가 설치되어 있고 일부가 작동 중이면 'workingPartially', 일부가 작동 중이면 'workingPartially', 액세스 포인트가 설치되어 있고 일부가 작동하지 않으면 'noService'입니다. Enum:'noService, totalFailure, working, workingPartially'  . Model: [https://schema.org/Text](https://schema.org/Text)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
필수 속성  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
이 데이터 모델은 [발렌시아 시청](https://www.valencia.es)과 협력하여 개발되었습니다.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 속성에 대한 데이터 모델 설명  
알파벳순으로 정렬(자세한 내용을 보려면 클릭)  
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
## 페이로드 예시  
#### WifiPointOfInterest NGSI-v2 키-값 예시  
다음은 키-값으로 JSON-LD 형식의 와이파이 포인트 오브 인터레스트의 예시입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
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
#### WifiPointOfInterest NGSI-v2 정규화 예제  
다음은 정규화된 JSON-LD 형식의 와이파이 포인트 오브 인터레스트의 예시입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
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
#### WifiPointOfInterest NGSI-LD 키-값 예시  
다음은 키-값으로 JSON-LD 형식의 와이파이 포인트 오브 인터레스트의 예시입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
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
#### WifiPointOfInterest NGSI-LD 정규화 예제  
다음은 정규화된 JSON-LD 형식의 와이파이 포인트 오브 인터레스트의 예시입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
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
[FAQ 10](https://smartdatamodels.org/index.php/faqs/)을 참조하여 규모 단위를 다루는 방법에 대한 답변을 확인하세요.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
