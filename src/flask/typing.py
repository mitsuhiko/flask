import typing as t


if t.TYPE_CHECKING:
    from werkzeug.datastructures import Headers  # noqa: F401
    from wsgiref.types import WSGIApplication  # noqa: F401
    from .wrappers import Response  # noqa: F401
    from .views import View  # noqa: F401

# The possible types that are directly convertible or are a Response object.
ResponseValue = t.Union[
    "Response",
    t.AnyStr,
    t.Dict[str, t.Any],  # any jsonify-able dict
    t.Generator[t.AnyStr, None, None],
]
StatusCode = int

# the possible types for an individual HTTP header
HeaderName = str
HeaderValue = t.Union[str, t.List[str], t.Tuple[str, ...]]

# the possible types for HTTP headers
HeadersValue = t.Union[
    "Headers", t.Dict[HeaderName, HeaderValue], t.List[t.Tuple[HeaderName, HeaderValue]]
]

# The possible types returned by a route function.
ResponseReturnValue = t.Union[
    ResponseValue,
    t.Tuple[ResponseValue, HeadersValue],
    t.Tuple[ResponseValue, StatusCode],
    t.Tuple[ResponseValue, StatusCode, HeadersValue],
    "WSGIApplication",
]

AppOrBlueprintKey = t.Optional[str]  # The App key is None, whereas blueprints are named
AfterRequestCallable = t.Callable[["Response"], "Response"]
BeforeRequestCallable = t.Callable[[], None]
ErrorHandlerCallable = t.Callable[[Exception], ResponseReturnValue]
TeardownCallable = t.Callable[[t.Optional[BaseException]], "Response"]
TemplateContextProcessorCallable = t.Callable[[], t.Dict[str, t.Any]]
TemplateFilterCallable = t.Callable[[t.Any], str]
TemplateGlobalCallable = t.Callable[[], t.Any]
TemplateTestCallable = t.Callable[[t.Any], bool]
URLDefaultCallable = t.Callable[[str, dict], None]
URLValuePreprocessorCallable = t.Callable[[t.Optional[str], t.Optional[dict]], None]
ViewFuncArgument = t.Optional[t.Union[t.Callable, t.Type["View"]]]
