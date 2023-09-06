<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティWifiPointOfInterest  
=========================<!-- /10-Header -->  
<!-- 15-License -->  
[オープン・ライセンス](https://github.com/smart-data-models//dataModel.WifiNetwork/blob/master/WifiPointOfInterest/LICENSE.md)  
[文書は自動的に生成される](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバル記述：**このエンティティは、無線ネットワークを持つ Point of Interest を記述する。  
バージョン: 0.1.0  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## プロパティのリスト  

<sup><sub>[*] 属性に型がない場合は、複数の型があるか、異なるフォーマット/パターンがある可能性があるためです</sub></sup>。  
- `address[object]`: 郵送先住所  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 国。例えば、スペイン  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 番地がある地域と、その地域に含まれる地域  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: その地域がある地域、またその国がある地域  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 地区とは行政区画の一種で、国によっては地方自治体によって管理されている。    
	- `postOfficeBoxNumber[string]`: 私書箱の住所のための私書箱番号。例：03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 郵便番号。例：24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 番地  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
- `alternateName[string]`: この項目の別名  - `areaServed[string]`: サービスまたは提供品が提供される地理的地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `category[array]`: このポイントのカテゴリー。許容される値：Factual taxonomy](https://github.com/Factual/places/blob/master/categories/factual_taxonomy.json)によって定義されたものと、データモデルのユーザが実装できるその他のカテゴリ。  . Model: [https://schema.org/Number](https://schema.org/Number)- `clientsConnected[number]`: このポイントに接続しているクライアントまたはユーザーの数  . Model: [https://schema.org/Number](https://schema.org/Number)- `dataProvider[string]`: ハーモナイズされたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated[date-time]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified[date-time]`: エンティティの最終変更のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: この商品の説明  - `email[idn-email]`: 所有者のEメールアドレス  - `id[*]`: エンティティの一意識別子  - `location[*]`: アイテムへの Geojson 参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygon のいずれか。  - `name[string]`: このアイテムの名前  - `owner[array]`: 所有者の固有IDを参照するJSONエンコードされた文字列を含むリスト。  - `seeAlso[*]`: アイテムに関する追加リソースを指すURIのリスト  - `service[array]`: この属性は、無線サービスを受ける1つまたは複数の自治体のサービス部門にアクセスポイントを割り当てるために使用されます。例えば図書館、博物館、社会福祉、スポーツ  . Model: [https://schema.org/Number](https://schema.org/Number)- `source[string]`: エンティティ・データの元のソースを URL として示す一連の文字。ソース・プロバイダの完全修飾ドメイン名、またはソース・オブジェクトの URL を推奨する。  - `timeInstant[date-time]`: ペイロードのタイムスタンプ。本番環境では、属性タイプが `ISO8601` 文字列と等しい場合がある。その場合、`DateTime`の同義語と見なさなければならない。この属性は、古い FIWARE リファレンス実装との後方互換性のために保持される。  . Model: [https://schema.org/Datetime](https://schema.org/Datetime)- `type[string]`: NGSIエンティティタイプ。WifiPointOfInterestでなければならない。  - `wifiStatus[string]`: この場所に利用可能なワイヤレスネットワークがあるかどうか、およびそのサービスが提供されているかどうかを示します。許可される値は次のとおりです：アクセスポイントがインストールされていない場合は「noService」、アクセスポイントがインストールされており、そのすべてが動作している（アップ）場合は「working」、アクセスポイントがインストールされており、そのすべてが動作していない（ダウン）場合は「totalFailure」、アクセスポイントがインストールされており、その一部が動作（アップ）しており、その一部が動作していない（ダウン）場合は「workingPartially」である。Enum:'noService'、'totalFailure'、'working'、'workingPartially'  . Model: [https://schema.org/Text](https://schema.org/Text)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
必須プロパティ  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
このデータモデルは、[バレンシア市役所](https://www.valencia.es)と協力して開発された。  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## プロパティのデータモデル記述  
アルファベット順（クリックで詳細表示）  
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
## ペイロードの例  
#### WifiPointOfInterest NGSI-v2 キー値の例  
WifiPointOfInterestのJSON-LD形式のkey-valuesの例である。これはNGSI-v2と互換性があり、`options=keyValues`を使用すると、個々のエンティティのコンテキストデータを返す。  
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
#### WifiPointOfInterest NGSI-v2 正規化例  
以下は、正規化された JSON-LD 形式の WifiPointOfInterest の例である。これは、オプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
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
#### WifiPointOfInterest NGSI-LD キー値の例  
以下はWifiPointOfInterestをJSON-LD形式でkey-valuesとした例である。options=keyValues`を使うとNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返す。  
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
#### WifiPointOfInterest NGSI-LD 正規化例  
以下は、正規化された JSON-LD 形式の WifiPointOfInterest の例である。これは、オプションを使用しない場合はNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
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
マグニチュード単位の扱い方については、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照のこと。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
