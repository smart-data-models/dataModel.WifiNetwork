<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
엔티티: 액세스 포인트    
============<!-- /10-Header -->    
<!-- 15-License -->    
[오픈 라이선스](https://github.com/smart-data-models//dataModel.WifiNetwork/blob/master/AccessPoint/LICENSE.md)    
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
글로벌 설명: **이 엔티티는 무선 네트워크를 생성하고 다른 Wi-Fi 장치가 연결할 수 있도록 하는 네트워킹 하드웨어인 액세스 포인트를 설명합니다**.    
버전: 0.1.1    
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
- `alternateName[string]`: 이 항목의 대체 이름  - `apState[string]`: 열거형:'위, 아래'. 액세스 포인트가 작동 중인지(값: up), 아니면 작동하지 않거나 종료되었는지(값: down)를 나타냅니다. Enum:'up, down'  . Model: [http://schema.org/Text](http://schema.org/Text)- `areaServed[string]`: 서비스 또는 제공 품목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)- `category[array]`: 센서: 빛, 동작, 온도 변화 등 물리적 환경의 이벤트나 변화를 감지하고 이에 반응하는 장치 https://w3id.org/saref#Sensor. 액추에이터 : 메커니즘이나 시스템을 움직이거나 제어하는 역할을 하는 장치 https://w3id.org/saref#Actuator. 계량기 : 사람이 읽을 수 있는 형태로 수량을 정확하게 감지하고 표시하도록 제작된 장치. SAREF에서 부분적으로 정의. HVAC: 실내 환경의 쾌적함을 제공하는 난방, 환기 및 에어컨(HVAC) 장치. https://w3id.org/saref#HVAC. 네트워크: LAN 또는 센서 네트워크의 허브, 스위치 또는 라우터와 같이 네트워크에서 다른 장치를 연결하는 데 사용되는 장치. (https://w3id.org/saref#Network. 멀티미디어 : 오디오, 이미지, 애니메이션, 비디오와 같은 멀티미디어 콘텐츠를 표시, 저장, 녹화 또는 재생하도록 설계된 장치. 열거형: '액추에이터, 비콘, 엔드건, HVAC, 구현, irrSection, irrSystem, 미터, 멀티미디어, 네트워크, 센서'. 원시 카테고리는 더 이상 사용되지 않습니다. 카테고리라는 이름의 다른 어트리뷰트와의 충돌을 피하기 위해 대신 deviceCategory를 사용하십시오.  . Model: [https://schema.org/Text](https://schema.org/Text)- `clientsConnected[number]`: 액세스 포인트에 연결된 클라이언트 또는 사용자 수  . Model: [https://schema.org/Number](https://schema.org/Number)- `controlledProperty[array]`: 감지, 측정 또는 제어할 수 있는 모든 항목입니다. Enum:'공기오염, 대기압력, 평균속도, 배터리수명, 배터리수급, cdom, 컨덕턴스, 전도도, 깊이, 먹는활동, 전기소비량, 에너지, 충전량레벨, 무료염소, 가스소비량, 게이트개방, 방향, 습도, 빛, 위치, 착유, 동작, 이동활동, 소음레벨, 점유, orp, pH, 전력, 강수량, 압력, 굴절지수, 염분, 연기, 토양수분, 태양복사, 속도, tds, 온도, 교통흐름, tss, 탁도, 물소비량, 물흐름, 물레벨, 물오염, 날씨조건, 무게, 바람방향, 바람속도'  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateInstalled[date-time]`: 장치를 설치한 시점을 나타내는 타임스탬프(설치가 필요한 경우)  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateLastReboot[date-time]`: 장치가 성공적으로 재부팅된 마지막 시간을 나타내는 타임스탬프입니다.  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateLastValueReported[date-time]`: 디바이스가 클라우드에 데이터를 성공적으로 보고한 마지막 시간을 나타내는 타임스탬프입니다.  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `description[string]`: 이 항목에 대한 설명  - `deviceCategory[array]`: 센서: 빛, 동작, 온도 변화 등 물리적 환경의 이벤트나 변화를 감지하고 이에 반응하는 장치 https://w3id.org/saref#Sensor. 액추에이터 : 메커니즘이나 시스템을 움직이거나 제어하는 역할을 하는 장치 https://w3id.org/saref#Actuator. 계량기 : 사람이 읽을 수 있는 형태로 수량을 정확하게 감지하고 표시하도록 제작된 장치. SAREF에서 부분적으로 정의. HVAC: 실내 환경의 쾌적함을 제공하는 난방, 환기 및 에어컨(HVAC) 장치. https://w3id.org/saref#HVAC. 네트워크: LAN 또는 센서 네트워크의 허브, 스위치 또는 라우터와 같이 네트워크에서 다른 장치를 연결하는 데 사용되는 장치. (https://w3id.org/saref#Network. 멀티미디어 : 오디오, 이미지, 애니메이션, 비디오와 같은 멀티미디어 콘텐츠를 표시, 저장, 녹화 또는 재생하도록 설계된 장치. 열거형: '액추에이터, 비콘, 엔드건, HVAC, 구현, irrSection, irrSystem, 미터, 멀티미디어, 네트워크, 센서'. 원시 카테고리는 더 이상 사용되지 않습니다. 카테고리라는 이름의 다른 어트리뷰트와의 충돌을 피하기 위해 대신 deviceCategory를 사용하십시오.  . Model: [https://schema.org/Text](https://schema.org/Text)- `email[idn-email]`: 소유자의 이메일 주소  - `firmwareVersion[string]`: 이 장치의 펌웨어 버전  . Model: [https://schema.org/Text](https://schema.org/Text)- `hardwareVersion[string]`: 이 장치의 하드웨어 버전  . Model: [https://schema.org/Text](https://schema.org/Text)- `id[*]`: 엔티티의 고유 식별자  - `ipAddress[string]`: 디바이스의 IP 주소  . Model: [https://schema.org/Text](https://schema.org/Text)- `location[*]`: 항목에 대한 지오숀 참조입니다. 포인트, 라인 문자열, 다각형, 멀티포인트, 멀티라인 문자열 또는 멀티폴리곤일 수 있습니다.  - `macAddress[string]`: 장치의 MAC 주소  . Model: [https://schema.org/Text](https://schema.org/Text)- `modelName[string]`: 디바이스 모델명  . Model: [https://schema.org/Text](https://schema.org/Text)- `name[string]`: 이 항목의 이름  - `osVersion[string]`: 호스트 운영 체제 장치의 버전  . Model: [https://schema.org/Text](https://schema.org/Text)- `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `refPointOfInterest[*]`: 액세스 포인트가 위치하고 서비스를 제공하는 관심 지점입니다.  . Model: [https://schema.org/URL](https://schema.org/URL)- `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `serialNumber[string]`: 제조업체에서 부여한 일련 번호  . Model: [https://schema.org/serialNumber](https://schema.org/serialNumber)- `service[array]`: 이 속성은 무선 서비스를 수신하는 하나 또는 여러 지자체 서비스 부서에 액세스 포인트를 할당하는 데 사용됩니다. 예 도서관, 박물관, 사회 서비스, 스포츠  . Model: [https://schema.org/Text](https://schema.org/Text)- `softwareVersion[string]`: 이 장치의 소프트웨어 버전  . Model: [https://schema.org/Text](https://schema.org/Text)- `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 문자 시퀀스입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `ssid[array]`: 액세스 포인트가 생성하는 SSID(서비스 세트 식별자)의 이름 목록입니다. 하나의 액세스 포인트가 하나 또는 여러 개의 SSID를 생성할 수 있습니다.  . Model: [https://schema.org/Text](https://schema.org/Text)- `supportedProtocol[array]`: 지원되는 프로토콜 또는 네트워크  . Model: [3g, bluetooth, bluetooth LE, cat-m, coap, ec-gsm-iot, gprs, http, lwm2m, lora, lte-m, mqtt, nb-iot, onem2m, sigfox, ul20, websocket](3g, bluetooth, bluetooth LE, cat-m, coap, ec-gsm-iot, gprs, http, lwm2m, lora, lte-m, mqtt, nb-iot, onem2m, sigfox, ul20, websocket)- `timeInstant[date-time]`: 페이로드의 타임스탬프입니다. 프로덕션 환경에서는 속성 유형이 `ISO8601` 문자열과 같을 수 있습니다. 이 경우 `DateTime`의 동의어로 간주해야 합니다. 이 속성은 이전 FIWARE 참조 구현과의 하위 호환성을 위해 유지됩니다.  . Model: [https://schema.org/Datetime](https://schema.org/Datetime)- `type[string]`: NGSI 엔티티 유형. AccessPoint여야 합니다.  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
필수 속성    
- `id`  - `name`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
액세스 포인트는 건물 또는 장소(광장, 거리, 해변, 정원 등)에서 무선 네트워크를 제공할 수 있으며, 별도의 엔티티 유형 [WifiPointOfInterest](../../WifiPointOfInterest/)로 모델링됩니다. 이 데이터 모델은 [발렌시아 시청](https://www.valencia.es)과 협력하여 개발되었습니다.    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## 속성에 대한 데이터 모델 설명    
알파벳순으로 정렬(자세한 내용을 보려면 클릭)    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
AccessPoint:      
  description: This entity describes an Access Point which is a networking hardware that generates a wireless network and allows other Wi-Fi devices to connect to it      
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
      description: The geographic area where a service or offered item is provided      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    category:      
      description: "Sensor: A device that detects and responds to events or changes in the physical environment such as light, motion, or temperature changes. https://w3id.org/saref#Sensor. actuator : A device responsible for moving or controlling a mechanism or system. https://w3id.org/saref#Actuator. Meter : A device built to accurately detect and display a quantity in a form readable by a human being. Partially defined by SAREF. HVAC : Heating, Ventilation and Air Conditioning (HVAC) device that provides indoor environmental comfort. https://w3id.org/saref#HVAC. Network : A device used to connect other devices in a network, such as hub, switch or router in a LAN or Sensor network. (https://w3id.org/saref#Network. Multimedia : A device designed to display, store, record or play multimedia content such as audio, images, animation, video. Enum:'actuator, beacon, endgun, HVAC, implement, irrSection, irrSystem, meter, multimedia, network, sensor'. Raw category will be deprecated use deviceCategory instead to avoid conflict with other aqttributes named category"      
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
      description: Number of clients or users connected to the access point      
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
          - uvLampIntensity      
          - uvOrganicLoad      
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
    dateInstalled:      
      description: A timestamp which denotes when the device was installed (if it requires installation)      
      format: date-time      
      type: string      
      x-ngsi:      
        model: https://schema.org/DateTime      
        type: Property      
    dateLastReboot:      
      description: A timestamp which denotes the last time when the device was successfully rebooted      
      format: date-time      
      type: string      
      x-ngsi:      
        model: https://schema.org/DateTime      
        type: Property      
    dateLastValueReported:      
      description: A timestamp which denotes the last time when the device successfully reported data to the cloud      
      format: date-time      
      type: string      
      x-ngsi:      
        model: https://schema.org/DateTime      
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
    deviceCategory:      
      description: "Sensor: A device that detects and responds to events or changes in the physical environment such as light, motion, or temperature changes. https://w3id.org/saref#Sensor. actuator : A device responsible for moving or controlling a mechanism or system. https://w3id.org/saref#Actuator. Meter : A device built to accurately detect and display a quantity in a form readable by a human being. Partially defined by SAREF. HVAC : Heating, Ventilation and Air Conditioning (HVAC) device that provides indoor environmental comfort. https://w3id.org/saref#HVAC. Network : A device used to connect other devices in a network, such as hub, switch or router in a LAN or Sensor network. (https://w3id.org/saref#Network. Multimedia : A device designed to display, store, record or play multimedia content such as audio, images, animation, video. Enum:'actuator, beacon, endgun, HVAC, implement, irrSection, irrSystem, meter, multimedia, network, sensor'. Raw category will be deprecated use deviceCategory instead to avoid conflict with other aqttributes named category"      
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
    email:      
      description: Email address of owner      
      format: idn-email      
      type: string      
      x-ngsi:      
        type: Property      
    firmwareVersion:      
      description: The firmware version of this device      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    hardwareVersion:      
      description: The hardware version of this device      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
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
    ipAddress:      
      description: The IP address of the device      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
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
    macAddress:      
      description: The MAC address of the device      
      pattern: ^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    modelName:      
      description: Device's model name      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    name:      
      description: The name of this item      
      type: string      
      x-ngsi:      
        type: Property      
    osVersion:      
      description: The version of the host operating system device      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
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
    refPointOfInterest:      
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
      description: The point of interest where the access point is located and provides the service      
      x-ngsi:      
        model: https://schema.org/URL      
        type: Relationship      
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
    serialNumber:      
      description: The serial number assigned by the manufacturer      
      type: string      
      x-ngsi:      
        model: https://schema.org/serialNumber      
        type: Property      
    service:      
      description: 'This attribute is used to assign the access point to one or several municipal service departments that receive the wireless service. For example: Library, Museums, Social Services, Sports'      
      items:      
        type: string      
      type: array      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    softwareVersion:      
      description: The software version of this device      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    source:      
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'      
      type: string      
      x-ngsi:      
        type: Property      
    ssid:      
      description: List of the names of the SSID (service set identifier) that the access point generates. One access point can generate one or several SSID      
      items:      
        type: string      
      type: array      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    supportedProtocol:      
      description: Supported protocol(s) or networks      
      items:      
        enum:      
          - 3g      
          - bluetooth      
          - bluetooth LE      
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
      description: 'Timestamp of the payload . There can be production environments where the attribute type is equal to the `ISO8601` string. If so, it must be considered as a synonym of `DateTime`. This attribute is kept for backwards compatibility with old FIWARE reference implementations'      
      format: date-time      
      type: string      
      x-ngsi:      
        model: https://schema.org/Datetime      
        type: Property      
    type:      
      description: NGSI Entity type. It has to be AccessPoint      
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
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
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
## 페이로드 예시    
#### AccessPoint NGSI-v2 키-값 예제    
다음은 키-값으로 JSON-LD 형식의 액세스 포인트의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
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
#### AccessPoint NGSI-v2 정규화 예제    
다음은 정규화된 JSON-LD 형식의 액세스 포인트의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "ap_542",  
  "type": "AccessPoint",  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "addressLocality": "Valencia",  
      "streetAddress": "Avda. Plata, 26"  
    }  
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
      "coordinates": [  
        -0.367589,  
        39.454197  
      ]  
    }  
  },  
  "ssid": {  
    "type": "StructuredValue",  
    "value": [  
      "AVC",  
      "wifivalencia"  
    ]  
  },  
  "service": {  
    "type": "StructuredValue",  
    "value": [  
      "Bomberos"  
    ]  
  },  
  "refPointOfInterest": {  
    "type": "Text",  
    "value": "poi_226"  
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
    "type": "StructuredValue",  
    "value": [  
      "Ayuntamiento_de_Valencia"  
    ]  
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
#### AccessPoint NGSI-LD 키-값 예제    
다음은 키-값으로 JSON-LD 형식의 액세스 포인트의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
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
#### AccessPoint NGSI-LD 정규화 예제    
다음은 정규화된 JSON-LD 형식의 액세스 포인트의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
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
[FAQ 10](https://smartdatamodels.org/index.php/faqs/)을 참조하여 규모 단위를 다루는 방법에 대한 답변을 확인하세요.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
