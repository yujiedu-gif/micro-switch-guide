from __future__ import annotations

from itertools import product
from typing import Any

from core import normalize_keyword, stable_id
from topic_scope import classify_keyword


CATALOG_VERSION = "micro-switch-keyword-catalog-v1"


INDUSTRIAL_MACHINES = (
    "cnc milling machine", "cnc lathe", "cnc router", "laser cutting machine", "plasma cutting machine",
    "waterjet cutting machine", "injection molding machine", "blow molding machine", "extrusion machine",
    "thermoforming machine", "stamping press", "hydraulic press", "pneumatic press", "sheet metal brake",
    "power shear", "industrial saw", "drill press", "surface grinder", "cylindrical grinder", "wire edm machine",
    "die casting machine", "forging press", "textile loom", "knitting machine", "industrial sewing machine",
    "printing press", "paper cutting machine", "book binding machine", "labeling machine", "cartoning machine",
    "case packing machine", "pallet wrapping machine", "bottling machine", "filling machine", "capping machine",
    "bagging machine", "vacuum packaging machine", "food slicing machine", "dough mixing machine",
    "industrial mixer", "centrifuge", "material feeder", "vibratory feeder", "bucket elevator", "belt conveyor",
    "roller conveyor", "chain conveyor", "screw conveyor", "overhead conveyor", "palletizer", "depalletizer",
    "pick and place robot", "welding robot", "painting robot", "assembly robot", "collaborative robot",
    "automated guided vehicle", "warehouse shuttle", "stacker crane", "forklift mast", "scissor lift",
    "boom lift", "dock leveler", "industrial door", "machine guard", "rotary indexing table", "linear slide",
    "ball screw actuator", "pneumatic cylinder", "hydraulic cylinder", "electric linear actuator",
    "motorized valve", "damper actuator", "industrial boiler", "industrial furnace", "incinerator",
    "air compressor", "vacuum pump", "process pump", "sump pump", "water treatment skid",
)

MACHINE_CONTEXTS = ("travel limit", "guard interlock", "home position", "end of stroke")

MOTION_SYSTEMS = (
    "garage door opener", "sliding gate opener", "swing gate opener", "roller shutter", "automatic door",
    "revolving door", "elevator car", "elevator landing door", "escalator", "moving walkway", "dumbwaiter",
    "wheelchair lift", "stair lift", "vehicle lift", "car parking lift", "loading dock door", "security barrier",
    "turnstile", "access hatch", "fire damper", "smoke damper", "motorized blind", "motorized curtain",
    "adjustable desk", "hospital bed", "recliner chair", "massage chair", "power wheelchair", "mobility scooter",
    "satellite dish actuator", "solar tracker", "antenna rotator", "camera pan tilt unit", "stage lift",
)

MOTION_CONTEXTS = ("open position", "closed position", "travel limit")

APPLICATION_BASES = (
    "microwave door interlock", "washing machine door", "washing machine lid", "clothes dryer door",
    "dishwasher door latch", "refrigerator door", "freezer door", "oven door", "air fryer basket",
    "rice cooker lid", "pressure cooker lid", "coffee machine brew unit", "espresso machine drip tray",
    "ice maker position", "water dispenser lever", "vacuum cleaner brush head", "robot vacuum bumper",
    "air conditioner panel", "range hood damper", "food processor bowl lock", "blender jar interlock",
    "stand mixer head lock", "bread maker lid", "toaster carriage", "electric kettle lid",
    "garbage disposal reset mechanism", "dishwasher float", "washing machine water level mechanism",
    "dryer belt safety mechanism", "dryer lint filter interlock", "furnace access panel", "boiler access door",
    "air handler access panel", "dehumidifier water tank", "humidifier water level", "portable heater tip over",
    "electric fan oscillation limit", "ceiling fan pull mechanism", "sewing machine foot pedal",
    "washing machine imbalance mechanism", "refrigerator ice chute", "commercial freezer door",
    "vending machine delivery door", "vending machine coin return", "arcade joystick", "computer mouse button",
    "printer cover", "printer paper path", "copier door", "scanner lid", "document feeder paper path",
    "paper shredder bin interlock", "cash drawer position", "postal scale platform", "barcode scanner trigger",
    "brake pedal", "clutch pedal", "parking brake pedal", "accelerator pedal position stop", "door jamb",
    "hood latch", "trunk latch", "tailgate latch", "charging port door", "fuel filler door", "seat position",
    "seat belt buckle", "power window limit", "sunroof limit", "convertible roof limit", "sliding door latch",
    "gear selector park position", "shift lever position", "steering column lock", "glove box latch",
    "center console latch", "windshield wiper park position", "washer fluid level", "suspension height limit",
    "motorcycle brake lever", "motorcycle clutch lever", "motorcycle side stand", "motorcycle seat latch",
    "electric bicycle brake lever", "electric bicycle battery lock", "golf cart brake pedal",
    "forklift seat presence mechanism", "forklift parking brake", "tractor clutch pedal", "tractor seat presence",
    "combine harvester access panel", "lawn mower seat interlock", "lawn mower brake pedal",
    "snow blower auger control", "pressure washer trigger", "leaf blower throttle", "chainsaw brake mechanism",
    "aircraft landing gear monitor", "aircraft door closed monitor", "aircraft cargo door lock monitor",
    "aircraft flap position", "aircraft cockpit push button", "train door closed monitor", "railway point machine limit",
    "bus door position", "truck tail lift limit", "ambulance compartment door", "fire engine compartment door",
    "hospital bed rail position", "patient lift travel limit", "medical cart drawer", "infusion pump door",
    "laboratory centrifuge lid", "autoclave door interlock", "sterilizer door interlock", "incubator door",
    "medical refrigerator door", "x ray equipment travel limit", "dental chair position", "operating table position",
    "microscope stage limit", "laboratory analyzer cover", "sample tray position", "pill dispenser door",
    "atm cash cassette door", "safe door bolt position", "access control door position", "security gate limit",
    "fire alarm pull station", "emergency exit door position", "cabinet door position", "drawer closed position",
    "tool chest drawer interlock", "server rack door", "control cabinet door", "electrical enclosure door",
    "valve open position", "valve closed position", "damper open position", "damper closed position",
    "pressure switch mechanism", "temperature switch mechanism", "float switch mechanism",
    "joystick assembly", "foot switch assembly", "push button assembly", "toggle switch assembly",
)

APPLICATION_TEMPLATES = (
    "{base} micro switch", "{base} micro switch function", "how does a {base} micro switch work",
    "{base} micro switch location", "{base} micro switch symptoms", "{base} micro switch failure causes",
    "{base} micro switch not working", "{base} micro switch intermittent operation",
    "how to test a {base} micro switch", "{base} micro switch continuity test",
    "{base} micro switch NO and NC terminals", "{base} micro switch actuator travel",
    "{base} micro switch operating force", "{base} micro switch contact rating",
    "{base} micro switch wiring", "{base} micro switch replacement", "{base} micro switch adjustment",
    "{base} micro switch maintenance", "{base} micro switch troubleshooting", "how to select a {base} micro switch",
)

ACTUATORS = (
    "pin plunger", "spring plunger", "roller plunger", "straight lever", "short lever", "long lever",
    "hinge lever", "roller lever", "simulated roller lever", "leaf lever", "fork lever", "flexible rod",
    "panel mount plunger", "push button", "paddle lever", "rotary actuator", "wobble stick", "cam follower",
)

PARAMETERS = (
    "operating force", "release force", "total travel force", "pretravel", "overtravel", "movement differential",
    "operating position", "release position", "free position", "total travel position", "repeat accuracy",
    "mechanical life", "electrical life", "switching frequency", "contact resistance", "insulation resistance",
    "dielectric strength", "contact gap", "contact bounce", "actuation speed", "release speed", "hysteresis",
    "creepage distance", "clearance distance", "terminal strength", "actuator strength", "mounting torque",
    "vibration resistance", "shock resistance", "temperature range", "humidity resistance", "ingress protection",
)

ELECTRICAL_TOPICS = (
    "SPDT contacts", "SPST NO contacts", "SPST NC contacts", "DPDT contacts", "changeover contacts",
    "COM terminal", "NO terminal", "NC terminal", "silver alloy contacts", "gold plated contacts",
    "bifurcated contacts", "micro load switching", "resistive load rating", "inductive load rating",
    "motor load rating", "lamp load rating", "DC load switching", "AC load switching", "inrush current",
    "minimum switching current", "maximum switching current", "contact arcing", "contact welding",
    "arc suppression", "flyback diode", "RC snubber", "electrical noise", "signal level switching",
)

ENVIRONMENT_TOPICS = (
    "dust exposure", "water exposure", "oil exposure", "coolant exposure", "salt spray exposure",
    "corrosive atmosphere", "high humidity", "condensation", "freezing temperature", "high temperature",
    "thermal cycling", "mechanical vibration", "mechanical shock", "low air pressure", "high pressure washdown",
    "outdoor installation", "food processing environment", "medical equipment environment",
    "explosive atmosphere", "vacuum environment", "metal particle contamination", "flour dust contamination",
)

FAILURE_TOPICS = (
    "contact oxidation", "contact contamination", "contact wear", "contact welding", "spring fatigue",
    "actuator wear", "lever deformation", "roller wear", "plunger sticking", "housing cracks", "seal damage",
    "terminal looseness", "solder joint failure", "wire break", "intermittent continuity", "high contact resistance",
    "failure to release", "failure to actuate", "false triggering", "position drift", "excessive pretravel",
    "insufficient overtravel", "slow actuation", "rapid cycling", "mechanical misalignment", "cam misalignment",
    "mounting screw looseness", "water ingress", "dust ingress", "temperature damage",
)


def _application_bases() -> list[tuple[str, str]]:
    rows = [(f"{machine} {context}", "industrial_machine") for machine, context in product(INDUSTRIAL_MACHINES, MACHINE_CONTEXTS)]
    rows += [(f"{system} {context}", "motion_system") for system, context in product(MOTION_SYSTEMS, MOTION_CONTEXTS)]
    rows += [(base, "specific_application") for base in APPLICATION_BASES]
    return rows


def _technical_keywords() -> list[tuple[str, str, str]]:
    rows: list[tuple[str, str, str]] = []
    for actuator in ACTUATORS:
        for template in (
            "{x} micro switch", "{x} micro switch working principle", "{x} micro switch applications",
            "{x} micro switch selection", "{x} micro switch adjustment", "{x} micro switch travel",
            "{x} micro switch operating force", "{x} micro switch failure", "how to test a {x} micro switch",
            "{x} micro switch installation",
        ):
            rows.append((template.format(x=actuator), "actuator", actuator))
    for category, topics in (("parameter", PARAMETERS), ("electrical", ELECTRICAL_TOPICS), ("environment", ENVIRONMENT_TOPICS), ("failure", FAILURE_TOPICS)):
        for topic in topics:
            for template in (
                "micro switch {x}", "micro switch {x} explained", "how to check micro switch {x}",
                "micro switch {x} troubleshooting", "micro switch {x} causes", "micro switch {x} prevention",
                "micro switch {x} selection", "micro switch {x} testing",
            ):
                rows.append((template.format(x=topic), category, topic))
    return rows


def catalog_candidates(target: int, existing: set[str], known_brands: list[str]) -> list[dict[str, Any]]:
    application_raw: list[tuple[str, str, str, str]] = []
    bases = _application_bases()
    for template_index, template in enumerate(APPLICATION_TEMPLATES):
        for base, category in bases:
            application_raw.append((template.format(base=base), category, base, f"application:{template_index}"))
    technical_raw = [
        (keyword, category, topic, f"technical:{category}")
        for keyword, category, topic in _technical_keywords()
    ]

    output: list[dict[str, Any]] = []
    seen = set(existing)

    def add(rows: list[tuple[str, str, str, str]], limit: int) -> None:
        for keyword, category, subject, template_id in rows:
            if len(output) >= limit:
                break
            normalized = normalize_keyword(keyword)
            if normalized in seen:
                continue
            decision = classify_keyword(keyword, known_brands)
            if decision.decision != "accept":
                continue
            seen.add(normalized)
            output.append({
                "keyword_id": stable_id("kwc", f"{CATALOG_VERSION}:{normalized}"),
                "keyword": keyword,
                "normalized_keyword": normalized,
                "category": category,
                "subject": subject,
                "template_id": template_id,
                "decision": "accept",
                "scope_class": decision.scope_class,
                "reason_codes": [],
                "generator_version": CATALOG_VERSION,
            })

    # Reserve roughly ten percent for reusable technical concepts so the
    # catalog is not only an equipment-name expansion.
    technical_quota = min(len(technical_raw), max(1, target // 10))
    add(technical_raw, technical_quota)
    add(application_raw, target)
    return output
