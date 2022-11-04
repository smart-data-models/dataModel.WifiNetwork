<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体。访点  
=====<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.WifiNetwork/blob/master/AccessPoint/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全局描述。**该实体描述了一个接入点，它是一个网络硬件，生成一个无线网络，并允许其他Wi-Fi设备连接到它**。  
版本：0.1.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

##属性列表  

<sup><sub>[*] 如果一个属性中没有一个类型，是因为它可能有几种类型或不同的格式/模式</sub></sup>。  
- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: 这个项目的一个替代名称  - `apState[string]`: Enum:'up, down'.表示接入点是否在工作（值：up），或不工作或关闭（值：down）。Enum:'up, down'（向上，向下  . Model: [http://schema.org/Text](http://schema.org/Text)- `areaServed[string]`: 提供服务或提供项目的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `category[array]`: 传感器。探测并对物理环境中的事件或变化做出反应的设备，如光、运动或温度变化。https://w3id.org/saref#Sensor。执行器：负责移动或控制一个机制或系统的设备。https://w3id.org/saref#Actuator。计量器 : 为准确检测并以人类可读的形式显示某一数量而建造的设备。部分由SAREF定义。HVAC : 暖气、通风和空调（HVAC）设备，提供室内环境舒适度。https://w3id.org/saref#HVAC。网络 : 用于连接网络中其他设备的设备，如局域网或传感器网络中的集线器、交换机或路由器。(https://w3id.org/saref#Network.多媒体 :用于显示、存储、记录或播放多媒体内容的设备，如音频、图像、动画、视频。Enum:'actuator, beacon, endgun, HVAC, implement, irrSection, irrSystem, meter, multimedia, network, sensor'。  . Model: [https://schema.org/Text](https://schema.org/Text)- `clientsConnected[number]`: 连接到接入点的客户或用户的数量。  . Model: [https://schema.org/Number](https://schema.org/Number)- `controlledProperty[array]`: 任何可以被感知、测量或控制的东西。枚举。空气污染, 大气压力, 平均速度, 电池寿命, 电池供应, 电池容量, 电导率, 电导率, 深度, 饮食活动, 电力消耗, 能量, 填充水平, 自由氯, 气体消耗, 开门, 湿度, 光, 位置, 挤奶, 运动, 运动活动,噪声水平, 占用率, orp, pH值, 功率, 降水, 压力, 折射指数, 盐度, 烟雾, 土壤湿度, 太阳辐射, 速度, tds, 温度, 交通流量, tss, 浊度, 耗水量, 水流量, 水位, 水污染, 天气状况, 重量, 风向, 风速'  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 一串识别统一数据实体提供者的字符。  - `dateCreated[string]`: 实体创建时间戳。这通常会由存储平台分配。  - `dateInstalled[string]`: 一个时间戳，表示设备的安装时间（如果需要安装）。  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateLastReboot[string]`: 一个时间戳，表示设备最后一次成功重启的时间。  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateLastValueReported[string]`: 一个时间戳，表示设备最后一次向云端成功报告数据的时间。  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateModified[string]`: 实体最后一次修改的时间戳。这通常会由存储平台分配。  - `description[string]`: 对这个项目的描述  - `email[string]`: 业主的电子邮件地址。  - `firmwareVersion[string]`: 该设备的固件版本。  . Model: [https://schema.org/Text](https://schema.org/Text)- `hardwareVersion[string]`: 该设备的硬件版本。  . Model: [https://schema.org/Text](https://schema.org/Text)- `id[*]`: 实体的唯一标识符  - `ipAddress[string]`: 设备的IP地址。  . Model: [https://schema.org/Text](https://schema.org/Text)- `location[*]`: 对该项目的Geojson引用。它可以是点、线字符串、多边形、多点、多线字符串或多多边形。  - `macAddress[string]`: 设备的MAC地址。  . Model: [https://schema.org/Text](https://schema.org/Text)- `modelName[string]`: 设备的型号名称。  . Model: [https://schema.org/Text](https://schema.org/Text)- `name[string]`: 这个项目的名称。  - `osVersion[string]`: 主机操作系统设备的版本。  . Model: [https://schema.org/Text](https://schema.org/Text)- `owner[array]`: 一个包含JSON编码的字符序列的列表，引用所有者的唯一Ids。  - `refPointOfInterest[*]`: 接入点所在的兴趣点，并提供服务。  . Model: [https://schema.org/URL](https://schema.org/URL)- `seeAlso[*]`: 指向有关该项目的其他资源的URI列表  - `serialNumber[string]`: 制造商分配的序列号。  . Model: [https://schema.org/serialNumber](https://schema.org/serialNumber)- `service[array]`: 此属性用于将接入点分配给接受无线服务的一个或几个市政服务部门。比如说。图书馆、博物馆、社会服务、体育...  . Model: [https://schema.org/Text](https://schema.org/Text)- `softwareVersion[string]`: 该设备的软件版本。  . Model: [https://schema.org/Text](https://schema.org/Text)- `source[string]`: 一系列的字符，以URL的形式给出实体数据的原始来源。建议为源提供者的完全合格域名，或源对象的URL。  - `ssid[array]`: 接入点产生的SSID（服务集标识符）的名称列表。一个接入点可以生成一个或几个SSID。  . Model: [https://schema.org/Text](https://schema.org/Text)- `supportedProtocol[array]`: 支持的协议或网络  . Model: [3g, bluetooth, bluetooth LE, cat-m, coap, ec-gsm-iot, gprs, http, lwm2m, lora, lte-m, mqtt, nb-iot, onem2m, sigfox, ul20, websocket](3g, bluetooth, bluetooth LE, cat-m, coap, ec-gsm-iot, gprs, http, lwm2m, lora, lte-m, mqtt, nb-iot, onem2m, sigfox, ul20, websocket)- `timeInstant[string]`: 有效载荷的时间戳。在生产环境中，可能存在属性类型等于`ISO8601`字符串的情况。如果是这样，它必须被视为`DateTime`的同义词。保留这个属性是为了向后兼容旧的FIWARE参考实现。  . Model: [https://schema.org/Datetime](https://schema.org/Datetime)- `type[string]`: NGSI实体类型。它必须是AccessPoint  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
所需属性  
- `id`  - `name`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
接入点可以在一个建筑物或一个地方（广场、街道、海滩、花园......）提供无线网络，并以一个独立的实体类型[WifiPointOfInterest](.../.../WifiPointOfInterest/)进行建模。这个数据模型是与[瓦伦西亚市政厅](https://www.valencia.es)合作开发的。  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 数据模型的属性描述  
按字母顺序排列（点击查看详情）。  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
AccessPoint:    
  description: 'This entity describes an Access Point which is a networking hardware that generates a wireless network and allows other Wi-Fi devices to connect to it'    
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
    apState:    
      description: 'Enum:''up, down''. Indicates whether the access point is working (value: up), or it is not working or shut down (value: down). Enum:''up, down'''    
      enum:    
        - up    
        - down    
      type: string    
      x-ngsi:    
        model: http://schema.org/Text    
        type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    category:    
      description: "Sensor: A device that detects and responds to events or changes in the physical environment such as light, motion, or temperature changes. https://w3id.org/saref#Sensor. actuator : A device responsible for moving or controlling a mechanism or system. https://w3id.org/saref#Actuator. Meter : A device built to accurately detect and display a quantity in a form readable by a human being. Partially defined by SAREF. HVAC : Heating, Ventilation and Air Conditioning (HVAC) device that provides indoor environmental comfort. https://w3id.org/saref#HVAC. Network : A device used to connect other devices in a network, such as hub, switch or router in a LAN or Sensor network. (https://w3id.org/saref#Network. Multimedia : A device designed to display, store, record or play multimedia content such as audio, images, animation, video. Enum:'actuator, beacon, endgun, HVAC, implement, irrSection, irrSystem, meter, multimedia, network, sensor'"    
      items:    
        enum:    
          - actuator    
          - beacon    
          - endgun    
          - HVAC    
          - implement    
          - irrSection    
          - irrSystem    
          - meter    
          - multimedia    
          - network    
          - sensor    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    clientsConnected:    
      description: 'Number of clients or users connected to the access point.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    controlledProperty:    
      description: 'Anything that can be sensed, measured or controlled by. Enum:''airPollution, atmosphericPressure, averageVelocity, batteryLife, batterySupply, cdom, conductance, conductivity, depth, eatingActivity, electricityConsumption, energy, fillingLevel, freeChlorine, gasConsumption, gateOpening, heading, humidity, light, location, milking, motion, movementActivity, noiseLevel, occupancy, orp, pH, power, precipitation, pressure, refractiveIndex, salinity, smoke, soilMoisture, solarRadiation, speed, tds, temperature, trafficFlow, tss, turbidity, waterConsumption, waterFlow, waterLevel, waterPollution, weatherConditions, weight, windDirection, windSpeed'''    
      items:    
        enum:    
          - airPollution    
          - atmosphericPressure    
          - averageVelocity    
          - batteryLife    
          - batterySupply    
          - cdom    
          - conductance    
          - conductivity    
          - depth    
          - eatingActivity    
          - electricityConsumption    
          - energy    
          - fillingLevel    
          - freeChlorine    
          - gasConsumption    
          - gateOpening    
          - heading    
          - humidity    
          - light    
          - location    
          - milking    
          - motion    
          - movementActivity    
          - noiseLevel    
          - occupancy    
          - orp    
          - pH    
          - power    
          - precipitation    
          - pressure    
          - refractiveIndex    
          - salinity    
          - smoke    
          - soilMoisture    
          - solarRadiation    
          - speed    
          - tds    
          - temperature    
          - trafficFlow    
          - tss    
          - turbidity    
          - waterConsumption    
          - waterFlow    
          - waterLevel    
          - waterPollution    
          - weatherConditions    
          - weight    
          - windDirection    
          - windSpeed    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
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
    dateInstalled:    
      description: 'A timestamp which denotes when the device was installed (if it requires installation).'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    dateLastReboot:    
      description: 'A timestamp which denotes the last time when the device was successfully rebooted.'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    dateLastValueReported:    
      description: 'A timestamp which denotes the last time when the device successfully reported data to the cloud.'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
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
    firmwareVersion:    
      description: 'The firmware version of this device.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    hardwareVersion:    
      description: 'The hardware version of this device.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    id:    
      anyOf: &accesspoint_-_properties_-_owner_-_items_-_anyof    
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
    ipAddress:    
      description: 'The IP address of the device.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: 'GeoProperty. Geojson reference to the item. Point'    
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
        - description: 'GeoProperty. Geojson reference to the item. LineString'    
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
        - description: 'GeoProperty. Geojson reference to the item. Polygon'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiPoint'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiLineString'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiLineString'    
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
        type: GeoProperty    
    macAddress:    
      description: 'The MAC address of the device.'    
      pattern: ^([[A-Fa-f0-9]]{2}[:.-]?){5}[[A-Fa-f0-9]]{2}$    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    modelName:    
      description: 'Device''s model name.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    osVersion:    
      description: 'The version of the host operating system device.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *accesspoint_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    refPointOfInterest:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'The point of interest where the access point is located and provides the service.'    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Relationship    
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
    serialNumber:    
      description: 'The serial number assigned by the manufacturer.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/serialNumber    
        type: Property    
    service:    
      description: 'This attribute is used to assign the access point to one or several municipal service departments that receive the wireless service. For example: Library, Museums, Social Services, Sports...'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    softwareVersion:    
      description: 'The software version of this device.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    ssid:    
      description: 'List of the names of the SSID (service set identifier) that the access point generates. One access point can generate one or several SSID.'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    supportedProtocol:    
      description: 'Supported protocol(s) or networks'    
      items:    
        enum:    
          - 3g    
          - bluetooth    
          - 'bluetooth LE'    
          - cat-m    
          - coap    
          - ec-gsm-iot    
          - gprs    
          - http    
          - lwm2m    
          - lora    
          - lte-m    
          - mqtt    
          - nb-iot    
          - onem2m    
          - sigfox    
          - ul20    
          - websocket    
        type: string    
      type: array    
      x-ngsi:    
        model: '3g, bluetooth, bluetooth LE, cat-m, coap, ec-gsm-iot, gprs, http, lwm2m, lora, lte-m, mqtt, nb-iot, onem2m, sigfox, ul20, websocket'    
        type: Property    
    timeInstant:    
      description: 'Timestamp of the payload . There can be production environments where the attribute type is equal to the `ISO8601` string. If so, it must be considered as a synonym of `DateTime`. This attribute is kept for backwards compatibility with old FIWARE reference implementations.'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Datetime    
        type: Property    
    type:    
      description: 'NGSI Entity type. It has to be AccessPoint'    
      enum:    
        - AccessPoint    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - name    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.WifiNetwork/blob/master/AccessPoint/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.WifiNetwork/AccessPoint/schema.json    
  x-model-tags: ""    
  x-version: 0.1.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ＃＃＃＃有效载荷的例子  
#### AccessPoint NGSI-v2 关键值示例  
这里是一个以JSON-LD格式作为key-values的AccessPoint的例子。当使用`options=keyValues`时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "ap_542",  
  "type": "AccessPoint",  
  "address": {  
    "streetAddress": "Avda. Plata, 26",  
    "addressLocality": "Valencia"  
  },  
  "apState": "up",  
  "clientsConnected": 125,  
  "name": "Bomberos_ParqueCentral_Planta_1",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -0.367589,  
      39.454197  
    ]  
  },  
  "ssid": [  
    "AVC",  
    "wifivalencia"  
  ],  
  "clientsConnected": 258,  
  "service": [  
    "Bomberos"  
  ],  
  "refPointOfInterest": "poi_226",  
  "timeInstant": "2020-09-22T09:30:03.00Z",  
  "contactPoint": "asistencia_tecnica_wifi@valencia.es",  
  "dataProvider": "Airwave",  
  "dateInstalled": "2019-01-01T00:00:00.00Z",  
  "dateLastReboot": "2020-08-14T12:43:39.00Z",  
  "dateLastValueReported": "2020-09-22T09:30:03.00Z",  
  "description": "Situado en el Parque Central de Bomberos, planta 1",  
  "firmwareVersion": "7.2.584.0",  
  "hardwareVersion": "",  
  "ipAddress": "192.14.56.78",  
  "macAddress": "00:2E:89:25:78:05",  
  "modelName": "Aironet 1000 LWAPP",  
  "osVersion": "",  
  "owner": [  
    "Ayuntamiento_de_Valencia"  
  ],  
  "provider": "Cisco",  
  "serialNumber": "KWC33301C44",  
  "softwareVersion": "",  
  "source": "Cisco"  
}  
```  
</details>  
#### AccessPoint NGSI-v2规范化示例  
下面是一个以JSON-LD格式规范化的AccessPoint的例子。当不使用选项时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "ap_542",  
  "type": "AccessPoint",  
  "address": {  
    "type": "Text",    
    "value": "Avda. Plata, 26. Valencia"  
  },  
  "apState": {  
    "type": "Text",    
    "value": "up"  
  },  
  "clientsConnected": {  
    "type": "Number",      
    "value": 125  
  },  
  "name": {  
    "type": "Text",      
    "value": "Bomberos_ParqueCentral_Planta_1"  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [-0.367589, 39.454197]  
    }  
  },  
  "ssid": {  
    "type": "Array",  
    "value": ["AVC", "wifivalencia"]  
  },  
  "service": {  
    "type": "Array",  
    "value": ["Bomberos"]  
  },  
  "refPointOfInterest": {  
    "type": "Relationship",  
    "object": "poi_226"  
  },  
  "timeInstant": {  
    "type": "DateTime",  
    "value": "2020-09-22T09:30:03.00Z"  
  },  
  "contactPoint": {  
    "type": "Text",    
    "value": "asistencia_tecnica_wifi@valencia.es"  
  },  
  "dataProvider": {  
    "type": "Text",    
    "value": "Airwave"  
  },  
  "dateInstalled": {  
    "type": "DateTime",  
    "value": "2019-01-01T00:00:00.00Z"  
  },  
  "dateLastReboot": {  
    "type": "DateTime",  
    "value": "2020-08-14T12:43:39.00Z"  
  },  
  "dateLastValueReported": {  
    "type": "DateTime",  
    "value": "2020-09-22T09:30:03.00Z"  
  },  
  "description": {  
    "type": "Text",    
    "value": "Situado en el Parque Central de Bomberos, planta 1"  
  },  
  "firmwareVersion": {  
    "type": "Text",    
    "value": "7.2.584.0"  
  },  
  "hardwareVersion": {  
    "type": "Text",    
    "value": ""  
  },  
  "ipAddress": {  
    "type": "Text",    
    "value": "192.14.56.78"  
  },  
  "macAddress": {  
    "type": "Text",    
    "value": "00:2E:89:25:78:05"  
  },  
  "modelName": {  
    "type": "Text",     
    "value": "Aironet 1000 LWAPP"  
  },  
  "osVersion": {  
    "type": "Text",     
    "value": ""  
  },  
  "owner": {  
    "type": "Text",  
    "value": "Ayuntamiento_de_Valencia"  
  },  
  "provider": {  
    "type": "Text",     
    "value": "Cisco"  
  },  
  "serialNumber": {  
    "type": "Text",     
    "value": "KWC33301C44"  
  },  
  "softwareVersion": {  
    "type": "Text",     
    "value": ""  
  },  
  "source": {  
    "type": "Text",     
    "value": "Cisco"  
  }    
}  
```  
</details>  
#### AccessPoint NGSI-LD关键值示例  
这里是一个以JSON-LD格式作为key-values的AccessPoint的例子。当使用`options=keyValues`时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "ap_542",  
    "type": "AccessPoint",  
    "address": {  
        "streetAddress": "Avda. Plata, 26",  
        "addressLocality": "Valencia"  
    },  
    "apState": "up",  
    "clientsConnected": 258,  
    "contactPoint": "asistencia_tecnica_wifi@valencia.es",  
    "dataProvider": "Airwave",  
    "dateInstalled": "2019-01-01T00:00:00.00Z",  
    "dateLastReboot": "2020-08-14T12:43:39.00Z",  
    "dateLastValueReported": "2020-09-22T09:30:03.00Z",  
    "description": "Situado en el Parque Central de Bomberos, planta 1",  
    "firmwareVersion": "7.2.584.0",  
    "hardwareVersion": "",  
    "ipAddress": "192.14.56.78",  
    "location": {  
        "type": "Point",  
        "coordinates": [  
            -0.367589,  
            39.454197  
        ]  
    },  
    "macAddress": "00:2E:89:25:78:05",  
    "modelName": "Aironet 1000 LWAPP",  
    "name": "Bomberos_ParqueCentral_Planta_1",  
    "osVersion": "",  
    "owner": [  
        "Ayuntamiento_de_Valencia"  
    ],  
    "provider": "Cisco",  
    "refPointOfInterest": "poi_226",  
    "serialNumber": "KWC33301C44",  
    "service": [  
        "Bomberos"  
    ],  
    "softwareVersion": "",  
    "source": "Cisco",  
    "ssid": [  
        "AVC",  
        "wifivalencia"  
    ],  
    "timeInstant": "2020-09-22T09:30:03.00Z",  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.WifiNetwork/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### AccessPoint NGSI-LD规范化示例  
下面是一个以JSON-LD格式规范化的AccessPoint的例子。当不使用选项时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "ap_542",  
    "type": "AccessPoint",  
    "address": {  
        "type": "Property",  
        "value": "Avda. Plata, 26. Valencia"  
    },  
    "apState": {  
        "type": "Property",  
        "value": "up"  
    },  
    "clientsConnected": {  
        "type": "Property",  
        "value": 125  
    },  
    "contactPoint": {  
        "type": "Property",  
        "value": "asistencia_tecnica_wifi@valencia.es"  
    },  
    "dataProvider": {  
        "type": "Property",  
        "value": "Airwave"  
    },  
    "dateInstalled": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2019-01-01T00:00:00.00Z"  
        }  
    },  
    "dateLastReboot": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2020-08-14T12:43:39.00Z"  
        }  
    },  
    "dateLastValueReported": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2020-09-22T09:30:03.00Z"  
        }  
    },  
    "description": {  
        "type": "Property",  
        "value": "Situado en el Parque Central de Bomberos, planta 1"  
    },  
    "firmwareVersion": {  
        "type": "Property",  
        "value": "7.2.584.0"  
    },  
    "hardwareVersion": {  
        "type": "Property",  
        "value": ""  
    },  
    "ipAddress": {  
        "type": "Property",  
        "value": "192.14.56.78"  
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
    "macAddress": {  
        "type": "Property",  
        "value": "00:2E:89:25:78:05"  
    },  
    "modelName": {  
        "type": "Property",  
        "value": "Aironet 1000 LWAPP"  
    },  
    "name": {  
        "type": "Property",  
        "value": "Bomberos_ParqueCentral_Planta_1"  
    },  
    "osVersion": {  
        "type": "Property",  
        "value": ""  
    },  
    "owner": {  
        "type": "Property",  
        "value": "Ayuntamiento_de_Valencia"  
    },  
    "provider": {  
        "type": "Property",  
        "value": "Cisco"  
    },  
    "refPointOfInterest": {  
        "type": "Relationship",  
        "object": "poi_226"  
    },  
    "serialNumber": {  
        "type": "Property",  
        "value": "KWC33301C44"  
    },  
    "service": {  
        "type": "Property",  
        "value": [  
            "Bomberos"  
        ]  
    },  
    "softwareVersion": {  
        "type": "Property",  
        "value": ""  
    },  
    "source": {  
        "type": "Property",  
        "value": "Cisco"  
    },  
    "ssid": {  
        "type": "Property",  
        "value": [  
            "AVC",  
            "wifivalencia"  
        ]  
    },  
    "timeInstant": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2020-09-22T09:30:03.00Z"  
        }  
    }  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
参见[常见问题10](https://smartdatamodels.org/index.php/faqs/)，以获得关于如何处理量级单位的答案。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
