Entité : AccessPoint  
====================  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.WifiNetwork/blob/master/AccessPoint/LICENSE.md)  
Description globale : **Cette entité décrit un point d'accès qui est un matériel de mise en réseau qui génère un réseau sans fil et permet à d'autres dispositifs Wi-Fi de s'y connecter**.  

## Liste des propriétés  

- `TimeInstant`: [Timestamp](https://github.com/telefonicaid/iotagent-node-lib#TimeInstant) enregistré par l'agent IoT de FIWARE. Remarque : cet attribut n'a pas été harmonisé afin de conserver une compatibilité ascendante avec les implémentations de référence FIWARE actuelles.  - `address`: L'adresse postale  - `alternateName`: Un nom alternatif pour cet élément  - `apState`: Enum : "up, down". Indique si le point d'accès fonctionne (valeur : up), s'il ne fonctionne pas ou s'il est fermé (valeur : down). Enum : 'up, down'.  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `category`: Capteur : Un dispositif qui détecte et répond à des événements ou des changements dans l'environnement physique tels que la lumière, le mouvement ou les changements de température. https://w3id.org/saref#Sensor.  
Actionneur : Un dispositif chargé de déplacer ou de contrôler un mécanisme ou un système. https://w3id.org/saref#Actuator.  
Compteur : Un dispositif construit pour détecter avec précision et afficher une quantité sous une forme lisible par un être humain. Partiellement défini par SAREF. CVC : Dispositif de chauffage, de ventilation et de climatisation (CVC) qui assure le confort de l'environnement intérieur. https://w3id.org/saref#HVAC.  
Réseau : Un dispositif utilisé pour connecter d'autres dispositifs dans un réseau, comme un concentrateur, un commutateur ou un routeur dans un réseau local ou un réseau de capteurs. (https://w3id.org/saref#Network.  
Multimédia : Un dispositif conçu pour afficher, stocker, enregistrer ou lire un contenu multimédia tel que du son, des images, des animations, des vidéos. Enum : 'actuator, beacon, endgun, HVAC, implement, irrSection, irrSystem, meter, multimedia, network, sensor'.  - `clientsConnected`: Nombre de clients ou d'utilisateurs connectés au point d'accès.  - `controlledProperty`: Tout ce qui peut être détecté, mesuré ou contrôlé. Enum :'pollution de l'air, pression atmosphérique, cdom, conductance, conductivité, profondeur, activité alimentaire, consommation d'électricité, énergie, niveau de remplissage, consommation de gaz, cap, humidité, lumière, emplacement, traite, mouvement, activité de mouvement, niveau de bruit, occupation, orp, pH, puissance, précipitation, pression, salinité, fumée, humidité du sol, rayonnement solaire, vitesse, tds, température, tss, turbidité, consommation d'eau, pollution de l'eau, conditions météorologiques, poids, direction du vent, vitesse du vent".  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateInstalled`: Un horodatage qui indique quand le dispositif a été installé (s'il nécessite une installation).  - `dateLastReboot`: Un horodatage qui indique la dernière fois que le dispositif a été redémarré avec succès.  - `dateLastValueReported`: Un horodatage qui indique la dernière fois que le dispositif a transmis avec succès des données au nuage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `description`: Une description de cet article  - `email`: Adresse électronique du propriétaire.  - `firmwareVersion`: La version du micrologiciel de cet appareil.  - `hardwareVersion`: La version matérielle de cet appareil.  - `id`: Identifiant unique de l'entité  - `ipAddress`: L'adresse IP de l'appareil.  - `location`:   - `macAddress`: L'adresse MAC de l'appareil.  - `modelName`: Nom du modèle de l'appareil.  - `name`: Le nom de cet élément.  - `osVersion`: La version du dispositif du système d'exploitation hôte.  - `owner`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `refPointOfInterest`: Le point d'intérêt où le point d'accès est situé et fournit le service.  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur l'élément  - `serialNumber`: Le numéro de série attribué par le fabricant.  - `service`: Cet attribut est utilisé pour affecter le point d'accès à un ou plusieurs services municipaux qui reçoivent le service sans fil. Par exemple : Bibliothèque, Musées, Services sociaux, Sports...  - `softwareVersion`: La version du logiciel de cet appareil.  - `source`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `ssid`: Liste des noms des SSID (Service Set Identifier) que le point d'accès génère. Un point d'accès peut générer un ou plusieurs SSID.  - `supportedProtocol`: Protocole(s) ou réseaux pris en charge  - `type`: Type d'entité NGSI. Il doit s'agir d'AccessPoint    
Propriétés requises  
- `address`  - `clientsConnected`  - `id`  - `location`  - `name`  - `type`    
Le point d'accès peut fournir un réseau sans fil dans un bâtiment ou un lieu (place, rue, plage, jardin...) modélisé avec un type d'entité séparé [WifiPointOfInterest](../../WifiPointOfInterest/). Ce modèle de données a été développé en coopération avec la [Mairie de Valence] (https://www.valencia.es).  
## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
AccessPoint:    
  description: 'This entity describes an Access Point which is a networking hardware that generates a wireless network and allows other Wi-Fi devices to connect to it'    
  properties:    
    TimeInstant:    
      description: "[Timestamp](https://github.com/telefonicaid/iotagent-node-lib#TimeInstant) saved by FIWARE's IoT Agent. Note: This attribute has not been harmonized to keep backwards compatibility with current FIWARE reference implementations."    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: https://schema.org/DateTime    
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
    apState:    
      description: 'Enum:''up, down''. Indicates whether the access point is working (value: up), or it is not working or shut down (value: down). Enum:''up, down'''    
      enum:    
        - up    
        - down    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Text    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    category:    
      description: "Sensor: A device that detects and responds to events or changes in the physical environment such as light, motion, or temperature changes. https://w3id.org/saref#Sensor. \nactuator : A device responsible for moving or controlling a mechanism or system. https://w3id.org/saref#Actuator. \nMeter : A device built to accurately detect and display a quantity in a form readable by a human being. Partially defined by SAREF. HVAC : Heating, Ventilation and Air Conditioning (HVAC) device that provides indoor environmental comfort. https://w3id.org/saref#HVAC. \nNetwork : A device used to connect other devices in a network, such as hub, switch or router in a LAN or Sensor network. (https://w3id.org/saref#Network. \nMultimedia : A device designed to display, store, record or play multimedia content such as audio, images, animation, video. Enum:'actuator, beacon, endgun, HVAC, implement, irrSection, irrSystem, meter, multimedia, network, sensor'"    
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
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    clientsConnected:    
      description: 'Number of clients or users connected to the access point.'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    controlledProperty:    
      description: 'Anything that can be sensed, measured or controlled by. Enum:''airPollution, atmosphericPressure, cdom, conductance, conductivity, depth, eatingActivity, electricityConsumption, energy, fillingLevel, gasComsumption, heading, humidity, light, location, milking, motion, movementActivity, noiseLevel, occupancy, orp, pH, power, precipitation, pressure, salinity, smoke, soilMoisture, solarRadiation, speed, tds, temperature, tss, turbidity, waterConsumption, waterPollution, weatherConditions, weight, windDirection, windSpeed'''    
      items:    
        enum:    
          - airPollution    
          - atmosphericPressure    
          - cdom    
          - conductance    
          - conductivity    
          - depth    
          - eatingActivity    
          - electricityConsumption    
          - energy    
          - fillingLevel    
          - freeChlorine    
          - gasComsumption    
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
          - tss    
          - turbidity    
          - waterConsumption    
          - waterPollution    
          - weatherConditions    
          - weight    
          - windDirection    
          - windSpeed    
        type: string    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateInstalled:    
      description: 'A timestamp which denotes when the device was installed (if it requires installation).'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: https://schema.org/DateTime    
    dateLastReboot:    
      description: 'A timestamp which denotes the last time when the device was successfully rebooted.'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: https://schema.org/DateTime    
    dateLastValueReported:    
      description: 'A timestamp which denotes the last time when the device successfully reported data to the cloud.'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: https://schema.org/DateTime    
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
    firmwareVersion:    
      description: 'The firmware version of this device.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    hardwareVersion:    
      description: 'The hardware version of this device.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
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
      type: Property    
    ipAddress:    
      description: 'The IP address of the device.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
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
    macAddress:    
      description: 'The MAC address of the device.'    
      pattern: ^([[:xdigit:]]{2}[:.-]?){5}[[:xdigit:]]{2}$    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    modelName:    
      description: 'Device''s model name.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    name:    
      description: 'The name of this item.'    
      type: Property    
    osVersion:    
      description: 'The version of the host operating system device.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *accesspoint_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
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
      type: Relationship    
      x-ngsi:    
        model: https://schema.org/URL    
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
    serialNumber:    
      description: 'The serial number assigned by the manufacturer.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/serialNumber    
    service:    
      description: 'This attribute is used to assign the access point to one or several municipal service departments that receive the wireless service. For example: Library, Museums, Social Services, Sports...'    
      items:    
        type: string    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    softwareVersion:    
      description: 'The software version of this device.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    ssid:    
      description: 'List of the names of the SSID (service set identifier) that the access point generates. One access point can generate one or several SSID.'    
      items:    
        type: string    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
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
      type: Property    
      x-ngsi:    
        model: '3g, bluetooth, bluetooth LE, cat-m, coap, ec-gsm-iot, gprs, http, lwm2m, lora, lte-m, mqtt, nb-iot, onem2m, sigfox, ul20, websocket'    
    type:    
      description: 'NGSI Entity type. It has to be AccessPoint'    
      enum:    
        - AccessPoint    
      type: Property    
  required:    
    - id    
    - type    
    - name    
    - address    
    - location    
    - clientsConnected    
  type: object    
```  
</details>    
## Exemples de charges utiles  
#### AccessPoint NGSI-v2 valeurs-clés Exemple  
Voici un exemple d'un AccessPoint au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
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
    "coordinates": [-0.367589, 39.454197]  
  },  
  "ssid": ["AVC", "wifivalencia"],  
  "clientsConnected": 258,  
  "service": ["Bomberos"],  
  "refPointOfInterest": "poi_226",  
  "TimeInstant": "2020-09-22T09:30:03.00Z",  
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
  "owner": ["Ayuntamiento_de_Valencia"],  
  "provider": "Cisco",  
  "serialNumber": "KWC33301C44",  
  "softwareVersion": "",  
  "source": "Cisco"  
}  
```  
#### AccessPoint NGSI-v2 normalisé Exemple  
Voici un exemple d'un AccessPoint au format JSON-LD tel que normalisé. Ce format est compatible avec la NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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
#### AccessPoint NGSI-LD key-values Exemple  
Voici un exemple d'un AccessPoint au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-LD lorsque vous utilisez `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
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
  "TimeInstant": "2020-09-22T09:30:03.00Z",  
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
  "source": "Cisco",  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
#### AccessPoint NGSI-LD normalisé Exemple  
Voici un exemple d'un AccessPoint au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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
  "name": {  
    "type": "Property",  
    "value": "Bomberos_ParqueCentral_Planta_1"  
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
  "ssid": {  
    "type": "Property",  
    "value": [  
      "AVC",  
      "wifivalencia"  
    ]  
  },  
  "service": {  
    "type": "Property",  
    "value": [  
      "Bomberos"  
    ]  
  },  
  "refPointOfInterest": {  
    "type": "Relationship",  
    "object": "poi_226"  
  },  
  "TimeInstant": {  
    "type": "Property",  
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
  "macAddress": {  
    "type": "Property",  
    "value": "00:2E:89:25:78:05"  
  },  
  "modelName": {  
    "type": "Property",  
    "value": "Aironet 1000 LWAPP"  
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
  "serialNumber": {  
    "type": "Property",  
    "value": "KWC33301C44"  
  },  
  "softwareVersion": {  
    "type": "Property",  
    "value": ""  
  },  
  "source": {  
    "type": "Property",  
    "value": "Cisco"  
  }  
}  
```  
