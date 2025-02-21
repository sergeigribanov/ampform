"""Abbreviated the annotations generated by sphinx-autodoc.

It's not necessary to generate the full path of type hints, because they are rendered as
clickable links.

See also https://github.com/sphinx-doc/sphinx/issues/5868.
"""
# pyright: reportMissingImports=false
from __future__ import annotations

from typing import TYPE_CHECKING

import sphinx.domains.python
from docutils import nodes
from sphinx.addnodes import pending_xref

if TYPE_CHECKING:
    from sphinx.environment import BuildEnvironment

__TARGET_SUBSTITUTIONS = {
    "BuilderReturnType": "ampform.dynamics.builder.BuilderReturnType",
    "FourMomenta": "ampform.kinematics.lorentz.FourMomenta",
    "FourMomentumSymbol": "ampform.kinematics.lorentz.FourMomentumSymbol",
    "InteractionProperties": "qrules.quantum_numbers.InteractionProperties",
    "LatexPrinter": "sympy.printing.printer.Printer",
    "Literal[(-1, 1)]": "typing.Literal",
    "NumPyPrinter": "sympy.printing.printer.Printer",
    "ParameterValue": "ampform.helicity.ParameterValue",
    "Particle": "qrules.particle.Particle",
    "ReactionInfo": "qrules.transition.ReactionInfo",
    "Slider": "symplot.Slider",
    "State": "qrules.transition.State",
    "StateTransition": "qrules.transition.StateTransition",
    "Topology": "qrules.topology.Topology",
    "WignerD": "sympy.physics.quantum.spin.WignerD",
    "a set-like object providing a view on D's items": "typing.ItemsView",
    "a set-like object providing a view on D's keys": "typing.KeysView",
    "ampform.helicity._T": "typing.TypeVar",
    "an object providing a view on D's values": "typing.ValuesView",
    "sp.Basic": "sympy.core.basic.Basic",
    "sp.Expr": "sympy.core.expr.Expr",
    "sp.Float": "sympy.core.numbers.Float",
    "sp.Indexed": "sympy.tensor.indexed.Indexed",
    "sp.IndexedBase": "sympy.tensor.indexed.IndexedBase",
    "sp.Rational": "sympy.core.numbers.Rational",
    "sp.Symbol": "sympy.core.symbol.Symbol",
    "sp.acos": "sympy.functions.elementary.trigonometric.acos",
    "sympy.printing.numpy.NumPyPrinter": "sympy.printing.printer.Printer",
    "typing.Literal[-1, 1]": "typing.Literal",
    "typing_extensions.Protocol": "typing.Protocol",
}
__REF_TYPE_SUBSTITUTIONS = {
    "DecoratedClass": "obj",
    "DecoratedExpr": "obj",
    "None": "obj",
    "RangeDefinition": "obj",
    "ampform.dynamics.builder.BuilderReturnType": "obj",
    "ampform.helicity.ParameterValue": "obj",
    "ampform.helicity.align.dpd.T": "obj",
    "ampform.kinematics.lorentz.FourMomenta": "obj",
    "ampform.kinematics.lorentz.FourMomentumSymbol": "obj",
    "ampform.sympy.DecoratedClass": "obj",
    "ampform.sympy.DecoratedExpr": "obj",
    "symplot.Slider": "obj",
}


try:  # Sphinx >=4.4.0
    # https://github.com/sphinx-doc/sphinx/blob/v4.4.0/sphinx/domains/python.py#L110-L133
    from sphinx.addnodes import pending_xref_condition
    from sphinx.domains.python import parse_reftarget

    def _new_type_to_xref(
        target: str,
        env: BuildEnvironment | None = None,  # type: ignore[assignment]
        suppress_prefix: bool = False,
    ) -> pending_xref:
        reftype, target, title, refspecific = parse_reftarget(target, suppress_prefix)
        target = __TARGET_SUBSTITUTIONS.get(target, target)
        reftype = __REF_TYPE_SUBSTITUTIONS.get(target, reftype)
        assert env is not None
        return pending_xref(
            "",
            *__create_nodes(env, title),
            refdomain="py",
            reftype=reftype,
            reftarget=target,
            refspecific=refspecific,
            **__get_env_kwargs(env),
        )

except ImportError:  # Sphinx <4.4.0
    # https://github.com/sphinx-doc/sphinx/blob/v4.3.2/sphinx/domains/python.py#L83-L107
    def _new_type_to_xref(
        target: str,
        env: BuildEnvironment | None = None,  # type: ignore[assignment]
        suppress_prefix: bool = False,
    ) -> pending_xref:
        target = __TARGET_SUBSTITUTIONS.get(target, target)
        reftype = __REF_TYPE_SUBSTITUTIONS.get(target, "class")
        assert env is not None
        return pending_xref(
            "",
            *__create_nodes(env, target),
            refdomain="py",
            reftype=reftype,
            reftarget=target,
            **__get_env_kwargs(env),
        )


def __get_env_kwargs(env: BuildEnvironment) -> dict:
    if env:
        return {
            "py:module": env.ref_context.get("py:module"),
            "py:class": env.ref_context.get("py:class"),
        }
    return {}


def __create_nodes(env: BuildEnvironment, title: str) -> list[nodes.Node]:
    short_name = title.split(".")[-1]
    if env.config.python_use_unqualified_type_names:
        return [
            pending_xref_condition("", short_name, condition="resolved"),
            pending_xref_condition("", title, condition="*"),
        ]
    return [nodes.Text(short_name)]


def relink_references() -> None:
    sphinx.domains.python.type_to_xref = _new_type_to_xref
