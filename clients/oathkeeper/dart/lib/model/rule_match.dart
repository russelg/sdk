//
// AUTO-GENERATED FILE, DO NOT MODIFY!
//
// @dart=2.0

// ignore_for_file: unused_element, unused_import
// ignore_for_file: always_put_required_named_parameters_first
// ignore_for_file: lines_longer_than_80_chars

part of openapi.api;

class RuleMatch {
  /// Returns a new [RuleMatch] instance.
  RuleMatch({
    this.methods = const [],
    this.url,
  });

  /// An array of HTTP methods (e.g. GET, POST, PUT, DELETE, ...). When ORY Oathkeeper searches for rules to decide what to do with an incoming request to the proxy server, it compares the HTTP method of the incoming request with the HTTP methods of each rules. If a match is found, the rule is considered a partial match. If the matchesUrl field is satisfied as well, the rule is considered a full match.
  List<String> methods;

  /// This field represents the URL pattern this rule matches. When ORY Oathkeeper searches for rules to decide what to do with an incoming request to the proxy server, it compares the full request URL (e.g. https://mydomain.com/api/resource) without query parameters of the incoming request with this field. If a match is found, the rule is considered a partial match. If the matchesMethods field is satisfied as well, the rule is considered a full match.  You can use regular expressions in this field to match more than one url. Regular expressions are encapsulated in brackets < and >. The following example matches all paths of the domain `mydomain.com`: `https://mydomain.com/<.*>`.
  String url;

  @override
  bool operator ==(Object other) => identical(this, other) || other is RuleMatch &&
     other.methods == methods &&
     other.url == url;

  @override
  int get hashCode =>
    (methods == null ? 0 : methods.hashCode) +
    (url == null ? 0 : url.hashCode);

  @override
  String toString() => 'RuleMatch[methods=$methods, url=$url]';

  Map<String, dynamic> toJson() {
    final json = <String, dynamic>{};
    if (methods != null) {
      json[r'methods'] = methods;
    }
    if (url != null) {
      json[r'url'] = url;
    }
    return json;
  }

  /// Returns a new [RuleMatch] instance and imports its values from
  /// [json] if it's non-null, null if [json] is null.
  static RuleMatch fromJson(Map<String, dynamic> json) => json == null
    ? null
    : RuleMatch(
        methods: json[r'methods'] == null
          ? null
          : (json[r'methods'] as List).cast<String>(),
        url: json[r'url'],
    );

  static List<RuleMatch> listFromJson(List<dynamic> json, {bool emptyIsNull, bool growable,}) =>
    json == null || json.isEmpty
      ? true == emptyIsNull ? null : <RuleMatch>[]
      : json.map((dynamic value) => RuleMatch.fromJson(value)).toList(growable: true == growable);

  static Map<String, RuleMatch> mapFromJson(Map<String, dynamic> json) {
    final map = <String, RuleMatch>{};
    if (json?.isNotEmpty == true) {
      json.forEach((key, value) => map[key] = RuleMatch.fromJson(value));
    }
    return map;
  }

  // maps a json object with a list of RuleMatch-objects as value to a dart map
  static Map<String, List<RuleMatch>> mapListFromJson(Map<String, dynamic> json, {bool emptyIsNull, bool growable,}) {
    final map = <String, List<RuleMatch>>{};
    if (json?.isNotEmpty == true) {
      json.forEach((key, value) {
        map[key] = RuleMatch.listFromJson(value, emptyIsNull: emptyIsNull, growable: growable,);
      });
    }
    return map;
  }
}

