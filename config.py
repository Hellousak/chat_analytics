prefix_mapping = {
    'f': 'Function',
    'd': 'Documents',
    'tp': 'Technical parameters',
    's': 'Solution',
    'm': 'Mechanical paramaters',

}

# slovník subkategorií
category_tree = {
    'Product': {
        'intercom': ['ip_vario', 'ip_force', 'ip_base', 'ip_verso', 'ip_one', 'ip_style', 'ip_uni', 'ip_safety', 'ip_solo'],
        'indoor_station': ['indoor_talk', 'indoor_touch', 'indoor_view', 'clip', 'ip_handset', 'indoor_compact'],
        'software': ['ip_eye', 'network_scanner', 'access_commander', 'my2n_management_platform', 'my2n_app',
                         'meeting_room', 'appear', 'picard_commander', 'elevator_center', 'call_centre', 'netstar'],
        'lift': ['lift1', 'lift2', 'easygate_ip', 'easygate_pro', 'lift8', 'liftgate', 'sentrio', 'liftip_2.0'],
        'other_product': ['voiceblue_next', 'sip_speaker_(horn)']
        }
    }



excluded_tags = {'lead', 'lead_h', 'None', 'ter', 'high', 'suspect_created','suspect_updated', 'contact_created', 'contact_updated', 'petr'}

