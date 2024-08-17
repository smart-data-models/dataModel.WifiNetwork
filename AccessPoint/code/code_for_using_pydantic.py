from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import (
    AnyUrl,
    AwareDatetime,
    BaseModel,
    EmailStr,
    Field,
    RootModel,
    confloat,
    constr,
)


class Address(BaseModel):
    addressCountry: Optional[str] = Field(
        None, description='The country. For example, Spain'
    )
    addressLocality: Optional[str] = Field(
        None,
        description='The locality in which the street address is, and which is in the region',
    )
    addressRegion: Optional[str] = Field(
        None,
        description='The region in which the locality is, and which is in the country',
    )
    district: Optional[str] = Field(
        None,
        description='A district is a type of administrative division that, in some countries, is managed by the local government',
    )
    postOfficeBoxNumber: Optional[str] = Field(
        None,
        description='The post office box number for PO box addresses. For example, 03578',
    )
    postalCode: Optional[str] = Field(
        None, description='The postal code. For example, 24004'
    )
    streetAddress: Optional[str] = Field(None, description='The street address')
    streetNr: Optional[str] = Field(
        None, description='Number identifying a specific property on a public street'
    )


class ApState(Enum):
    up = 'up'
    down = 'down'


class CategoryEnum(Enum):
    actuator = 'actuator'
    beacon = 'beacon'
    endgun = 'endgun'
    HVAC = 'HVAC'
    implement = 'implement'
    irrSection = 'irrSection'
    irrSystem = 'irrSystem'
    meter = 'meter'
    multimedia = 'multimedia'
    network = 'network'
    sensor = 'sensor'


class ControlledPropertyEnum(Enum):
    airPollution = 'airPollution'
    atmosphericPressure = 'atmosphericPressure'
    averageVelocity = 'averageVelocity'
    batteryLife = 'batteryLife'
    batterySupply = 'batterySupply'
    cdom = 'cdom'
    conductance = 'conductance'
    conductivity = 'conductivity'
    depth = 'depth'
    eatingActivity = 'eatingActivity'
    electricityConsumption = 'electricityConsumption'
    energy = 'energy'
    fillingLevel = 'fillingLevel'
    freeChlorine = 'freeChlorine'
    gasConsumption = 'gasConsumption'
    gateOpening = 'gateOpening'
    heading = 'heading'
    humidity = 'humidity'
    light = 'light'
    location = 'location'
    milking = 'milking'
    motion = 'motion'
    movementActivity = 'movementActivity'
    noiseLevel = 'noiseLevel'
    occupancy = 'occupancy'
    orp = 'orp'
    pH = 'pH'
    power = 'power'
    precipitation = 'precipitation'
    pressure = 'pressure'
    refractiveIndex = 'refractiveIndex'
    salinity = 'salinity'
    smoke = 'smoke'
    soilMoisture = 'soilMoisture'
    solarRadiation = 'solarRadiation'
    speed = 'speed'
    tds = 'tds'
    temperature = 'temperature'
    trafficFlow = 'trafficFlow'
    tss = 'tss'
    turbidity = 'turbidity'
    uvLampIntensity = 'uvLampIntensity'
    uvOrganicLoad = 'uvOrganicLoad'
    waterConsumption = 'waterConsumption'
    waterFlow = 'waterFlow'
    waterLevel = 'waterLevel'
    waterPollution = 'waterPollution'
    weatherConditions = 'weatherConditions'
    weight = 'weight'
    windDirection = 'windDirection'
    windSpeed = 'windSpeed'


class DeviceCategoryEnum(Enum):
    actuator = 'actuator'
    beacon = 'beacon'
    endgun = 'endgun'
    HVAC = 'HVAC'
    implement = 'implement'
    irrSection = 'irrSection'
    irrSystem = 'irrSystem'
    meter = 'meter'
    multimedia = 'multimedia'
    network = 'network'
    sensor = 'sensor'


class Type(Enum):
    Point = 'Point'


class Location(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[float] = Field(..., min_length=2)
    type: Type


class Coordinate(RootModel[List[float]]):
    root: List[float]


class Type1(Enum):
    LineString = 'LineString'


class Location1(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[Coordinate] = Field(..., min_length=2)
    type: Type1


class Type2(Enum):
    Polygon = 'Polygon'


class Location2(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type2


class Type3(Enum):
    MultiPoint = 'MultiPoint'


class Location3(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[float]]
    type: Type3


class Type4(Enum):
    MultiLineString = 'MultiLineString'


class Location4(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type4


class Type5(Enum):
    MultiPolygon = 'MultiPolygon'


class Location5(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[List[Coordinate]]]
    type: Type5


class SupportedProtocolEnum(Enum):
    field_3g = '3g'
    bluetooth = 'bluetooth'
    bluetooth_LE = 'bluetooth LE'
    cat_m = 'cat-m'
    coap = 'coap'
    ec_gsm_iot = 'ec-gsm-iot'
    gprs = 'gprs'
    http = 'http'
    lwm2m = 'lwm2m'
    lora = 'lora'
    lte_m = 'lte-m'
    mqtt = 'mqtt'
    nb_iot = 'nb-iot'
    onem2m = 'onem2m'
    sigfox = 'sigfox'
    ul20 = 'ul20'
    websocket = 'websocket'


class Type6(Enum):
    AccessPoint = 'AccessPoint'


class AccessPoint(BaseModel):
    address: Optional[Address] = Field(None, description='The mailing address')
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    apState: Optional[ApState] = Field(
        None,
        description="Enum:'up, down'. Indicates whether the access point is working (value: up), or it is not working or shut down (value: down). Enum:'up, down'",
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    category: Optional[List[CategoryEnum]] = Field(
        None,
        description="Sensor: A device that detects and responds to events or changes in the physical environment such as light, motion, or temperature changes. https://w3id.org/saref#Sensor. actuator : A device responsible for moving or controlling a mechanism or system. https://w3id.org/saref#Actuator. Meter : A device built to accurately detect and display a quantity in a form readable by a human being. Partially defined by SAREF. HVAC : Heating, Ventilation and Air Conditioning (HVAC) device that provides indoor environmental comfort. https://w3id.org/saref#HVAC. Network : A device used to connect other devices in a network, such as hub, switch or router in a LAN or Sensor network. (https://w3id.org/saref#Network. Multimedia : A device designed to display, store, record or play multimedia content such as audio, images, animation, video. Enum:'actuator, beacon, endgun, HVAC, implement, irrSection, irrSystem, meter, multimedia, network, sensor'. Raw category will be deprecated use deviceCategory instead to avoid conflict with other aqttributes named category",
    )
    clientsConnected: Optional[confloat(ge=0.0)] = Field(
        None, description='Number of clients or users connected to the access point'
    )
    controlledProperty: Optional[List[ControlledPropertyEnum]] = Field(
        None,
        description="Anything that can be sensed, measured or controlled by. Enum:'airPollution, atmosphericPressure, averageVelocity, batteryLife, batterySupply, cdom, conductance, conductivity, depth, eatingActivity, electricityConsumption, energy, fillingLevel, freeChlorine, gasConsumption, gateOpening, heading, humidity, light, location, milking, motion, movementActivity, noiseLevel, occupancy, orp, pH, power, precipitation, pressure, refractiveIndex, salinity, smoke, soilMoisture, solarRadiation, speed, tds, temperature, trafficFlow, tss, turbidity, waterConsumption, waterFlow, waterLevel, waterPollution, weatherConditions, weight, windDirection, windSpeed'",
    )
    dataProvider: Optional[str] = Field(
        None,
        description='A sequence of characters identifying the provider of the harmonised data entity',
    )
    dateCreated: Optional[AwareDatetime] = Field(
        None,
        description='Entity creation timestamp. This will usually be allocated by the storage platform',
    )
    dateInstalled: Optional[AwareDatetime] = Field(
        None,
        description='A timestamp which denotes when the device was installed (if it requires installation)',
    )
    dateLastReboot: Optional[AwareDatetime] = Field(
        None,
        description='A timestamp which denotes the last time when the device was successfully rebooted',
    )
    dateLastValueReported: Optional[AwareDatetime] = Field(
        None,
        description='A timestamp which denotes the last time when the device successfully reported data to the cloud',
    )
    dateModified: Optional[AwareDatetime] = Field(
        None,
        description='Timestamp of the last modification of the entity. This will usually be allocated by the storage platform',
    )
    description: Optional[str] = Field(None, description='A description of this item')
    deviceCategory: Optional[List[DeviceCategoryEnum]] = Field(
        None,
        description="Sensor: A device that detects and responds to events or changes in the physical environment such as light, motion, or temperature changes. https://w3id.org/saref#Sensor. actuator : A device responsible for moving or controlling a mechanism or system. https://w3id.org/saref#Actuator. Meter : A device built to accurately detect and display a quantity in a form readable by a human being. Partially defined by SAREF. HVAC : Heating, Ventilation and Air Conditioning (HVAC) device that provides indoor environmental comfort. https://w3id.org/saref#HVAC. Network : A device used to connect other devices in a network, such as hub, switch or router in a LAN or Sensor network. (https://w3id.org/saref#Network. Multimedia : A device designed to display, store, record or play multimedia content such as audio, images, animation, video. Enum:'actuator, beacon, endgun, HVAC, implement, irrSection, irrSystem, meter, multimedia, network, sensor'. Raw category will be deprecated use deviceCategory instead to avoid conflict with other aqttributes named category",
    )
    email: Optional[EmailStr] = Field(None, description='Email address of owner')
    firmwareVersion: Optional[str] = Field(
        None, description='The firmware version of this device'
    )
    hardwareVersion: Optional[str] = Field(
        None, description='The hardware version of this device'
    )
    id: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description='Unique identifier of the entity')
    ipAddress: Optional[str] = Field(None, description='The IP address of the device')
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    macAddress: Optional[
        constr(pattern=r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$')
    ] = Field(None, description='The MAC address of the device')
    modelName: Optional[str] = Field(None, description="Device's model name")
    name: Optional[str] = Field(None, description='The name of this item')
    osVersion: Optional[str] = Field(
        None, description='The version of the host operating system device'
    )
    owner: Optional[
        List[
            Union[
                constr(
                    pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!,:\\\\]+$',
                    min_length=1,
                    max_length=256,
                ),
                AnyUrl,
            ]
        ]
    ] = Field(
        None,
        description='A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)',
    )
    refPointOfInterest: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(
        None,
        description='The point of interest where the access point is located and provides the service',
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    serialNumber: Optional[str] = Field(
        None, description='The serial number assigned by the manufacturer'
    )
    service: Optional[List[str]] = Field(
        None,
        description='This attribute is used to assign the access point to one or several municipal service departments that receive the wireless service. For example: Library, Museums, Social Services, Sports',
    )
    softwareVersion: Optional[str] = Field(
        None, description='The software version of this device'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    ssid: Optional[List[str]] = Field(
        None,
        description='List of the names of the SSID (service set identifier) that the access point generates. One access point can generate one or several SSID',
    )
    supportedProtocol: Optional[List[SupportedProtocolEnum]] = Field(
        None, description='Supported protocol(s) or networks'
    )
    timeInstant: Optional[AwareDatetime] = Field(
        None,
        description='Timestamp of the payload . There can be production environments where the attribute type is equal to the `ISO8601` string. If so, it must be considered as a synonym of `DateTime`. This attribute is kept for backwards compatibility with old FIWARE reference implementations',
    )
    type: Optional[Type6] = Field(
        None, description='NGSI Entity type. It has to be AccessPoint'
    )
