<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entität: AccessPoint  
====================<!-- /10-Header -->  
<!-- 15-License -->  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.WifiNetwork/blob/master/AccessPoint/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Globale Beschreibung: **Diese Entität beschreibt einen Access Point, eine Netzwerk-Hardware, die ein drahtloses Netzwerk generiert und anderen Wi-Fi-Geräten erlaubt, sich damit zu verbinden**  
Version: 0.1.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste der Eigenschaften  

<sup><sub>[*] Wenn es für ein Attribut keinen Typ gibt, liegt das daran, dass es mehrere Typen oder unterschiedliche Formate/Muster haben kann</sub></sup>.  
- `address[object]`: Die Postanschrift  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Ein alternativer Name für diesen Artikel  - `apState[string]`: Enum:'up, down'. Gibt an, ob der Zugangspunkt in Betrieb ist (Wert: up), oder ob er nicht in Betrieb oder abgeschaltet ist (Wert: down). Enum:'up, down'  . Model: [http://schema.org/Text](http://schema.org/Text)- `areaServed[string]`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  . Model: [https://schema.org/Text](https://schema.org/Text)- `category[array]`: Sensor: Ein Gerät, das Ereignisse oder Veränderungen in der physikalischen Umgebung wie Licht, Bewegung oder Temperaturveränderungen erkennt und darauf reagiert. https://w3id.org/saref#Sensor. Aktor: Ein Gerät, das für die Bewegung oder Steuerung eines Mechanismus oder Systems verantwortlich ist. https://w3id.org/saref#Actuator. Messgerät : Ein Gerät, das zur genauen Erfassung und Anzeige einer Größe in einer für den Menschen lesbaren Form dient. Teilweise durch SAREF definiert. HVAC : Heizungs-, Belüftungs- und Klimaanlagen (HVAC), die für ein angenehmes Raumklima sorgen. https://w3id.org/saref#HVAC. Netzwerk : Ein Gerät, das dazu dient, andere Geräte in einem Netzwerk zu verbinden, wie z. B. Hub, Switch oder Router in einem LAN oder Sensornetzwerk. (https://w3id.org/saref#Network. Multimedia : Ein Gerät zum Anzeigen, Speichern, Aufzeichnen oder Abspielen von Multimedia-Inhalten wie Audio, Bilder, Animationen, Video. Enum:'actuator, beacon, endgun, HVAC, implement, irrSection, irrSystem, meter, multimedia, network, sensor'  . Model: [https://schema.org/Text](https://schema.org/Text)- `clientsConnected[number]`: Anzahl der Clients oder Benutzer, die mit dem Zugangspunkt verbunden sind.  . Model: [https://schema.org/Number](https://schema.org/Number)- `controlledProperty[array]`: Alles, was von einem Sensor erfasst, gemessen oder kontrolliert werden kann. Enum:airPollution, atmosphericPressure, averageVelocity, batteryLife, batterySupply, cdom, conductance, conductivity, depth, eatingActivity, electricityConsumption, energy, fillingLevel, freeChlorine, gasConsumption, gateOpening, heading, humidity, light, location, milking, motion, motionActivity, noiseLevel, occupancy, orp, pH, power, precipitation, pressure, refractiveIndex, salinity, smoke, soilMoisture, solarRadiation, speed, tds, temperature, trafficFlow, tss, turbidity, waterConsumption, waterFlow, waterLevel, waterPollution, weatherConditions, weight, windDirection, windSpeed'  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit.  - `dateCreated[string]`: Zeitstempel der Entitätserstellung. Dieser wird in der Regel von der Speicherplattform zugewiesen.  - `dateInstalled[string]`: Ein Zeitstempel, der angibt, wann das Gerät installiert wurde (falls es installiert werden muss).  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateLastReboot[string]`: Ein Zeitstempel, der angibt, wann das Gerät das letzte Mal erfolgreich neu gebootet wurde.  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateLastValueReported[string]`: Ein Zeitstempel, der den letzten Zeitpunkt angibt, zu dem das Gerät erfolgreich Daten an die Cloud gemeldet hat.  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateModified[string]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description[string]`: Eine Beschreibung dieses Artikels  - `email[string]`: E-Mail Adresse des Eigentümers.  - `firmwareVersion[string]`: Die Firmware-Version dieses Geräts.  . Model: [https://schema.org/Text](https://schema.org/Text)- `hardwareVersion[string]`: Die Hardware-Version dieses Geräts.  . Model: [https://schema.org/Text](https://schema.org/Text)- `id[*]`: Eindeutiger Bezeichner der Entität  - `ipAddress[string]`: Die IP-Adresse des Geräts.  . Model: [https://schema.org/Text](https://schema.org/Text)- `location[*]`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `macAddress[string]`: Die MAC-Adresse des Geräts.  . Model: [https://schema.org/Text](https://schema.org/Text)- `modelName[string]`: Modellname des Geräts.  . Model: [https://schema.org/Text](https://schema.org/Text)- `name[string]`: Der Name dieses Artikels.  - `osVersion[string]`: Die Version des Host-Betriebssystems Gerät.  . Model: [https://schema.org/Text](https://schema.org/Text)- `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `refPointOfInterest[*]`: Der Punkt von Interesse, an dem sich der Zugangspunkt befindet und den Dienst anbietet.  . Model: [https://schema.org/URL](https://schema.org/URL)- `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `serialNumber[string]`: Die vom Hersteller vergebene Seriennummer.  . Model: [https://schema.org/serialNumber](https://schema.org/serialNumber)- `service[array]`: Dieses Attribut wird verwendet, um den Zugangspunkt einer oder mehreren kommunalen Dienststellen zuzuordnen, die den drahtlosen Dienst empfangen. Zum Beispiel: Bibliothek, Museen, Sozialdienste, Sport...  . Model: [https://schema.org/Text](https://schema.org/Text)- `softwareVersion[string]`: Die Softwareversion dieses Geräts.  . Model: [https://schema.org/Text](https://schema.org/Text)- `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Es wird empfohlen, den voll qualifizierten Domänennamen des Quellanbieters oder die URL des Quellobjekts zu verwenden.  - `ssid[array]`: Liste der Namen der SSID (Service Set Identifier), die der Zugangspunkt erzeugt. Ein Zugangspunkt kann eine oder mehrere SSID erzeugen.  . Model: [https://schema.org/Text](https://schema.org/Text)- `supportedProtocol[array]`: Unterstützte(s) Protokoll(e) oder Netzwerk(e)  . Model: [3g, bluetooth, bluetooth LE, cat-m, coap, ec-gsm-iot, gprs, http, lwm2m, lora, lte-m, mqtt, nb-iot, onem2m, sigfox, ul20, websocket](3g, bluetooth, bluetooth LE, cat-m, coap, ec-gsm-iot, gprs, http, lwm2m, lora, lte-m, mqtt, nb-iot, onem2m, sigfox, ul20, websocket)- `timeInstant[string]`: Zeitstempel der Nutzdaten. Es kann Produktionsumgebungen geben, in denen der Attributtyp der Zeichenfolge "ISO8601" entspricht. In diesem Fall ist es als Synonym für "DateTime" zu betrachten. Dieses Attribut wird aus Gründen der Abwärtskompatibilität mit alten FIWARE-Referenzimplementierungen beibehalten.  . Model: [https://schema.org/Datetime](https://schema.org/Datetime)- `type[string]`: NGSI-Entitätstyp. Es muss AccessPoint sein  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Erforderliche Eigenschaften  
- `id`  - `name`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Der Zugangspunkt kann ein drahtloses Netzwerk in einem Gebäude oder an einem Ort (Platz, Straße, Strand, Garten...) bereitstellen, das mit einem separaten Entitätstyp [WifiPointOfInterest](../../WifiPointOfInterest/) modelliert wird. Dieses Datenmodell wurde in Zusammenarbeit mit dem [Rathaus von Valencia] (https://www.valencia.es) entwickelt.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
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
## Beispiel-Nutzlasten  
#### AccessPoint NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel für einen AccessPoint im JSON-LD-Format als Key-Values. Dies ist mit NGSI-v2 kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
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
#### AccessPoint NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für einen AccessPoint im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
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
#### AccessPoint NGSI-LD-Schlüsselwerte Beispiel  
Hier ist ein Beispiel für einen AccessPoint im JSON-LD-Format als Key-Values. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
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
#### AccessPoint NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für einen AccessPoint im JSON-LD-Format in normalisierter Form. Dies ist mit NGSI-LD kompatibel, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
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
Siehe [FAQ 10] (https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
