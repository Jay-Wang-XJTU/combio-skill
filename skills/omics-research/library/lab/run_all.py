"""Run deterministic educational experiments and capture exact environment."""
from pathlib import Path
from datetime import datetime, timezone
import importlib.metadata as im
import importlib.util
import json, platform, sys, time
import numpy as np
from .statistics import pseudoreplication_demo, selection_demo
from .causal import causal_demo
from .spatial import spatial_demo
from .transport import transport_demo
from .flow import flow_demo


def dump(path, obj):
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2, allow_nan=False), encoding="utf-8")


def main():
    root = Path(__file__).resolve().parents[1]
    out = root/"results"
    out.mkdir(exist_ok=True)
    environment = {"python": sys.version, "platform": platform.platform(), "packages": {}}
    for name in ["numpy", "scipy", "torch", "pandas", "statsmodels", "scikit-learn", "pytest", "nbformat", "nbclient"]:
        try: environment["packages"][name] = im.version(name)
        except im.PackageNotFoundError: environment["packages"][name] = "not_installed"
    dump(out/"environment.json", environment)
    report = {"started_at_utc": datetime.now(timezone.utc).isoformat(), "experiments": {},
              "evidence_level": "synthetic_numerical_checks_only", "original_paper_reproductions": 0}
    for name, fn in [("independent_replicates", pseudoreplication_demo), ("multiple_testing", selection_demo),
                     ("causal_identification", causal_demo), ("spatial_measurement", spatial_demo),
                     ("optimal_transport", transport_demo), ("flow_matching", flow_demo)]:
        start = time.perf_counter()
        ans = fn(); ans["seconds"] = time.perf_counter()-start
        report["experiments"][name] = ans
        dump(out/f"{name}.json", ans)
        print(name, json.dumps(ans, ensure_ascii=False), flush=True)
    report["optional_upstream_runtime"] = {
        name: "installed_not_executed" if importlib.util.find_spec(module) else "not_run_missing_dependency"
        for name, module in [("POT", "ot"), ("Meta_flow_matching", "flow_matching"), ("moscot", "moscot"), ("NicheCompass", "nichecompass")]}
    report["finished_at_utc"] = datetime.now(timezone.utc).isoformat()
    dump(out/"execution_report.json", report)
    print("Wrote", out/"execution_report.json")

if __name__ == "__main__":
    main()
